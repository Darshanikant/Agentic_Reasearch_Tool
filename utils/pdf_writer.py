# utils/pdf_generator.py

from fpdf import FPDF
import os
from datetime import datetime

def save_summary_to_pdf(topic, summary, output_dir="report_samples"):
    """Creates and saves a PDF report from the summary."""
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"{topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join(output_dir, filename)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Research Report: {topic.title()}", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, summary)

    pdf.output(filepath)
    return filepath
