odoo.define('mail.systray.UserSuggestionMenu', function (require) {
"use strict";

var core = require('web.core');
var session = require('web.session');
var SystrayMenu = require('web.SystrayMenu');
var Widget = require('web.Widget');
var Menu = require('web.Menu');

const { Component } = owl;

var UserSuggestionMenu = Widget.extend({
    name: 'user_suggestion_menu',
    template:'mail.systray.UserSuggestionMenu',
    events: {
    },
    init: function () {
        this._super.apply(this, arguments);
        this.user_id = session.uid;
        this.available_suggestion = session.available_suggestion;
        this.current_month_avg = session.current_month_avg;
        this.current_month_suggestion = session.current_month_suggestion;
    },
});

SystrayMenu.Items.push(UserSuggestionMenu);

return UserSuggestionMenu;

});
