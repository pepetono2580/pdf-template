from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    for y in range(20, 297, 10):
        pdf.line(10, y, 200, y)

    # Set the footer for the master page
    pdf.ln(265)
    pdf.set_font(family="Times", size=8, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set the footer for the other pages
        pdf.ln(277)
        pdf.set_font(family="Times", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 297, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
