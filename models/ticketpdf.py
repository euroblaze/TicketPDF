from odoo import models, api

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    def action_generate_pdf(self):
        # Logic to generate PDF using report generation method
        self.env.ref('ticketpdf.ticketpdf_report').report_action(self)
