{
    "name": "TicketPDF",
    "version": "1.0",
    "author": "Shumal",
    "category": "Tools",
    "website": "https://odootech.in",
    "license": "AGPL-3",
    "summary": "Generate a PDF from a helpdesk ticket description",
    "depends": ["base", "helpdesk"],
    "data": [
        "report/ticketpdf_template.xml",
        "report/ticket_template.xml",
    ],
    "installable": True,
    "application": False,
}
