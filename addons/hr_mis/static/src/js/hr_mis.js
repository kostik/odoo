/**
 * Created by kostik on 2016-10-03.
 */
odoo.define('web.web_widget_imperial_length', function (require) {
    "use strict";

    var core = require('web.core');
    var widget = require('web.form_widgets');
    var FormView = require('web.FormView');

    var QWeb = core.qweb;
    var cm_per_foot = 30.48;
    var cm_per_inch = 2.54;

    var ImperialLength = widget.FieldChar.extend({

        init: function () {
            this._super.apply(this, arguments);
            this.set("value", "");
        },
        start: function () {
            this.on("change:effective_readonly", this, function () {
                this.display_field();
                this.render_value();
            });
            this.display_field();
            return this._super();
        },
        is_syntax_valid: function () {
            var $input = this.$('input');
            if (!this.get("effective_readonly") && $input.size() > 0) {
                var value = $input.val();
                if (!value) {
                    return true;
                }
                var re = /^(\d+)\s+(\d+(\.\d{1,2}))?$/; // i.e. 6 2.5
                var values;
                if ((values = re.exec(value)) !== null) {
                    value = parseInt(values[1]*cm_per_foot + values[2]*cm_per_inch);
                    $input.val(value);
                }
                return !isNaN(value) &&
                    parseInt(Number(value)) == value && !isNaN(parseInt(value, 10));
            }
            return true;
        },

        display_field: function () {
            var self = this;
            this.$el.html(QWeb.render("FieldChar", {widget: this}));
            if (!this.get("effective_readonly")) {
                this.$("input").change(function () {
                    self.internal_set_value(self.$("input").val()||"");
                });
            }
        },
        render_value: function () {
            if (this.get("effective_readonly")) {
                var val = this.get("value");
                var feet = val / cm_per_foot;
                this.$el.text(val + " cm (" + Math.floor(feet) + " ft " + Math.round((feet % 1) * 120) / 10 + " in)");
            } else {
                this.$("input").val(this.get("value"));
            }
        }
    });

    core.form_widget_registry.add('imperial_length', ImperialLength);

    return {
        ImperialLength: ImperialLength
    };
});
