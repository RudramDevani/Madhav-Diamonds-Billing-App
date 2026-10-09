from models.billscrap import htmlcode
import pdfkit

filename = "Invoice.pdf"

pdfkit.from_string(htmlcode, filename)
