# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from dateutil.relativedelta import relativedelta

import logging
_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    employee_rating_ids = fields.One2many('employee.rating', 'employee_id',
        string='Employee Ratings', copy=True)

    @api.model
    def _rating_notification_to_hr_cron(self):
        try:
            ctx = dict(self._context)
            user_ids = self.env['res.users'].sudo().search([])
            template_id = self.env.ref('tnc_hr_ratings.rating_notification_to_hr_email', raise_if_not_found=False)
            for user in user_ids:
                current_date = fields.Date.today()
                last_date = current_date + relativedelta(day=1, months=+1, days=-1)
                before_3_date_of_month = last_date - relativedelta(days=3)
                current_month = str(before_3_date_of_month.month)
                month_dict = dict(self.env['employee.rating'].sudo().fields_get(allfields=['month'])['month']['selection'])
                ctx['no_of_days'] = (before_3_date_of_month - current_date).days
                ctx['last_date'] = last_date
                ctx['year'] = str(before_3_date_of_month.year) or ''
                ctx['month'] = month_dict.get(current_month) or ''
                ctx['month_year'] = ctx['month'] + '-' + ctx['year']

                if user.has_group('hr.group_hr_manager') and template_id and current_date == before_3_date_of_month:
                    template_id.sudo().with_context(ctx).send_mail(user.id, force_send=True, raise_exception=False)
        except Exception as e:
            _logger.info(e)
