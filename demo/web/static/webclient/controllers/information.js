
var _ = parent._;
var parent_controller = parent.controller;
var commands = parent.commands;
var settings = parent.settings;

var controller = {
    // on document ready
    onReady: function() {
        this.resetLanguage();
    },

	// reset view's language
	resetLanguage: function() {
		$("#view_level").text(_("LEVEL: "));
		$("#view_exp").text(_("EXP: "));
		$("#view_hp").text(_("HP: "));
		$("#view_hunger").text(_("HUNGER: "));
		$("#view_vitality").text(_("VITALITY: "));
		$("#view_attack").text(_("ATTACK: "));
		$("#view_defence").text(_("DEFENCE: "));
		$("#view_head").text(_("HEAD: "));
		$("#view_hand").text(_("HAND: "));
		$("#view_chest").text(_("CHEST: "));
		$("#view_leg").text(_("LEG: "));
	},

    // Set player's basic information
    setInfo: function(name, icon) {
        $("#name").text(name);
        var url = settings.resource_url + icon;
        $("#obj_icon").attr("src", url);
    },

    // Set player character's information
    setStatus: function(level, exp, max_exp, hp, max_hp, hunger, hungerMax,
                         vitality, vitalityMax, attack, defence) {
        var hp_str = hp + "/" + max_hp;

        var exp_str = "--";
        if (max_exp > 0) {
            exp_str = exp + "/" + max_exp;
        }
        var hunger_str = "X";
        hunger_str = this.setHungerDescByValue(hunger);

        var vitality_str = "--";
        if(vitalityMax > 0){
            vitality_str = vitality + "/" + vitalityMax;
        }

        $("#level").text(level);
        $("#exp").text(exp_str);
        $("#hp").text(hp_str);
        $("#vitality").text(vitality_str);
        $("#hunger").text(hunger_str);
        $("#attack").text(attack);
        $("#defence").text(defence);
    },

    setHungerDescByValue:function(hunger){
        if(this.valueBetween(hunger,80,100))
            return _("HUNGER_FULL")
        if(this.valueBetween(hunger,50,80))
            return _("HUNGER_HIGH")
        if(this.valueBetween(hunger,30,50))
            return _("HUNGER_MEDIUM")
        if(this.valueBetween(hunger,10,30))
            return _("HUNGER_LOW")
        if(this.valueBetween(hunger,0,10))
            return _("HUNGER_DIE")
    },

    //check value in
    valueBetween:function (x, min, max) {
        return x>=min && x<=max;
    },

    // Set player's equipments.
    setEquipments(equipments) {
        for (var pos in equipments) {
            var equip = equipments[pos];
            var dbref = "";
            var name = "";
            if (equip) {
                dbref = equip["dbref"];
                name = equip["name"];
            }

            $("#" + pos)
                .data("dbref", dbref)
                .html(name);
        }
    },

    doLook: function(caller) {
        var dbref = $(caller).data("dbref");
        commands.doLook(dbref);
    },
};

$(document).ready(function() {
	controller.onReady();
});