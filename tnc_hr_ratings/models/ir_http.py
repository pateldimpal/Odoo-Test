# -*- coding: utf-8 -*-

from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        result["available_suggestion"] = request.env.user.available_suggestion
        result["current_month_avg"] = request.env.user.current_month_avg
        result["current_month_suggestion"] = request.env.user.current_month_suggestion
        return result
