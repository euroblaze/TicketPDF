from odoo import models,api

class TicketPdfReport(models.AbstractModel):
    _name = "report.ticketpdf.report_ticketpdf_document"
    _description = "TicketPDF Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        # Get necessary data and pass it to the report template
        tickets = self.env['helpdesk.ticket'].browse(docids)
        return {
            'doc_ids': tickets.ids,
            'doc_model': 'helpdesk.ticket',
            'data': data,
            'docs': tickets,
        }
