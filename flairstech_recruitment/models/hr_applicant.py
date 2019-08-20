from odoo import fields, models


class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    notice_period = fields.Char()
    interview_date = fields.Date()

