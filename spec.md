# TicketPDF Module Specification
## Module Overview
TicketPDF is an Odoo version 16 module designed to take the description from a helpdesk ticket and publish it into an A4 PDF, while maintaining the HTML formatting from the ticket description. The PDF will have a custom header and footer, including various ticket and company information.

## Functional Requirements
1. Retrieve the helpdesk ticket description, maintaining HTML formatting.
- Generate a PDF with A4 size.
- Include a header with the company logo (300x100 px).
- Add a footer with due-date, ticket title, responsible assignee, and page number.
- Name the generated file using the ticket number and title.
- PDF Header

## The header of the PDF should contain:

- A company logo of size 300x100 px.
## PDF Footer
The footer of the PDF should contain:

- The due-date of the helpdesk ticket (right-aligned).
- The title of the ticket (left-aligned, multi-line if necessary, max 50% of page-width).
- The responsible assignee's name and email address (right-aligned).
- The page number and total number of pages (right-aligned).
## File Naming
The generated PDF file should be named using the following convention:


´´ticket-number.title_of_the_ticket.pdf´´

## Implementation Details
### Technologies
- Python 3.8+
- Odoo 16
- Reportlab or similar library for PDF generation.
### Dependencies
- base
- helpdesk

### Example
Given a helpdesk ticket with the following details:

- Ticket number: 12345
- Title: Network Issue
- Description: <p>There is an intermittent network issue...</p>
- Due-date: 2023-05-01
- Responsible assignee: John Doe (john.doe@example.com)
- The generated PDF file should be named 12345.Network_Issue.pdf and include:

- A header with the company logo (300x100 px).
- The ticket description with maintained HTML formatting.
- A footer containing the due-date, ticket title, responsible assignee, and page number.
