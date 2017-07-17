from muddery.typeclasses.player_characters import MudderyPlayerCharacter
from evennia import TICKER_HANDLER
from evennia.utils import gametime


class DLCharacter(MudderyPlayerCharacter):
    def at_post_puppet(self):
        TICKER_HANDLER.add(1, self.update_player_properties)
        super(DLCharacter, self).at_post_puppet()

    def at_post_unpuppet(self, player, session=None):
        TICKER_HANDLER.remove(1, self.update_player_properties)

    def update_player_properties(self):
        self.update_hunger()
        self.update_vitality()
        message = {"status": self.return_status()}
        self.msg(message)

    def after_data_loaded(self):
        super(DLCharacter, self).after_data_loaded()
        self.last_game_time = 0.0

    def update_hunger(self):
        """
        update character hunger value
        """
        gametime_passed = (gametime.gametime() - self.last_game_time)
        # 28800s-> 8hour realtime=>game time 48hour ->2days
        # 2 days(gametime) will reduce 100 point hunger
        if gametime_passed > (gametime.TIMEFACTOR * 288):
            self.last_game_time = gametime.gametime()
            if self.cattr.hunger > 0:
                self.cattr.hunger = self.cattr.hunger - 1
            else:
                self.cattr.hunger = 0
            if self.cattr.hunger >= self.cattr.hungerMax:
                self.cattr.hunger = self.cattr.hungerMax
                # self.msg({"msg": "Debug: gameTime:%s|last_game_time:%s" % (gametime.gametime(), gametime_passed)})

    def update_vitality(self):
        """
        update reduce the vitality per/s
        :return: 
        """
        if self.cattr.vitality > 0:
            # temp add 1 per second.
            self.cattr.vitality = self.cattr.vitality + 1
        else:
            self.cattr.vitality = 0
        if self.cattr.vitality >= self.cattr.vitalityMax:
            self.cattr.vitality = self.cattr.vitalityMax

    def move_to(self, destination, quiet=False,
                emit_to_obj=None, use_destination=True, to_none=False, move_hooks=True):
        """
        Moves this object to a new location.
        """

        # test
        if self.cattr.vitality > 10:
            # cost player vitality temp 10
            if self.cattr.vitality > 0:
                self.cattr.vitality = self.db.vitality - 10
            if self.cattr.vitality < 0:
                self.cattr.vitality = 0

            if (not quiet) and self.solo_mode:
                # If in solo mode, move quietly.
                quiet = True
            return super(DLCharacter, self).move_to(destination,
                                                               quiet,
                                                               emit_to_obj,
                                                               use_destination,
                                                               to_none,
                                                               move_hooks)
        else:
            self.msg({"msg": _("Fail to Moving")})
            self.show_location()
