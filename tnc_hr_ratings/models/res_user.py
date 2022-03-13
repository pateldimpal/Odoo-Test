# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _compute_current_month_suggestion(self):
        for rec in self:
            rec.current_month_avg = 0.0
            rec.current_month_suggestion = ''
            current_date = fields.Date.today()
            rec.available_suggestion = False
            last_rating_id = self.env['employee.rating'].sudo().search([
                ('year', '=', current_date.year), ('month', '=', str(current_date.month)),
                ('employee_id', '=', rec.employee_id.id)], order='review_date desc, id desc', limit=1)
            if last_rating_id:
                rec.available_suggestion = bool(last_rating_id)
                rec.current_month_avg = last_rating_id.per_month_average
                rec.current_month_suggestion = last_rating_id.review_comment

    available_suggestion = fields.Boolean(string="Available Suggestion ?", compute=_compute_current_month_suggestion)
    current_month_avg = fields.Float(string="Avg. of Current Month", compute=_compute_current_month_suggestion)
    current_month_suggestion = fields.Text("Current Month Suggestion", compute=_compute_current_month_suggestion)
