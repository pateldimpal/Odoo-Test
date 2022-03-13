# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class EmployeeRating(models.Model):
    _name = "employee.rating"
    _description = "Employee Ratings"

    def _compute_per_month_average(self):
        for rec in self:
            rec.per_month_average = 0.0
            rating_ids = self.env['employee.rating'].sudo().search([('year', '=', rec.year),
                ('month', '=', rec.month), ('employee_id', '=', rec.employee_id.id)]).mapped('rating')
            if rating_ids:
                len_of_ids = len(rating_ids)
                rec.per_month_average = sum([int(l) for l in rating_ids if l])/len_of_ids

    employee_id = fields.Many2one('hr.employee', string="Employee",
        required=True, ondelete='cascade')
    department_id = fields.Many2one('hr.department', 'Department', related="employee_id.department_id")
    job_id = fields.Many2one('hr.job', 'Job Position', related="employee_id.job_id")
    month = fields.Selection([('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'),
        ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'),
        ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December'), ],
        string='Month')
    year = fields.Char(string="Year")
    review_date = fields.Date('Date of Review', copy=False)
    rating = fields.Selection([('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'),
        ('4', '4'), ('5', '5')], string="Rating", tracking=True)
    review_comment = fields.Text(string="Review Comments")
    per_month_average = fields.Float(string="Avg. of Month", compute=_compute_per_month_average, group_operator="avg")

    _sql_constraints = [
        ('code_review_date_uniq', 'unique (employee_id, review_date)', 'The employee rating of \
            the review date must be unique per employee !'),
    ]

    @api.onchange('review_date')
    def _onchange_review_date(self):
        if self.review_date:
            self.year = self.review_date.year
            self.month = str(self.review_date.month)

    def name_get(self):
        result = []
        for rec in self:
            name = ''
            if rec.employee_id and rec.month and rec.year:
                month = dict(rec.fields_get(allfields=['month'])['month']['selection'])[rec.month]
                name = rec.employee_id.name + ' [' + month + '-' + rec.year +']'
            result.append((rec.id, name))
        return result
