from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

print("Enter PDF Name with .pdf at the end of name: ")
pdfname = input(">> ")
canvas = Canvas(pdfname, pagesize=LETTER)
canvas.drawString(2 * inch, 8 * inch, "")
canvas.save()
