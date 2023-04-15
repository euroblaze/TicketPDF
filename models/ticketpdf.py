from odoo import models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    def action_generate_pdf(self):
        # Logic to generate PDF using report generation method
        self.env.ref('ticketpdf.ticketpdf_report').report_action(self)

    # def _get_report_base_filename(self):
    #     return f'{str(self.ticket_ref)}-{self.ticket_name}.pdf'
