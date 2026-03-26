from PyPDF2 import PdfWriter
import os

try:
    merger = PdfWriter()

    filepath = os.path.join(os.path.dirname(__file__), "merge-pdf")

    pdf_list = [
        os.path.join(filepath, f) for f in os.listdir(filepath) if f.endswith(".pdf")
    ]

    for pdf in pdf_list:
        merger.append(pdf)  # for appending the pdfs to merger object

    # merger.encrypt("123456")  # Optional: Set a password for the merged PDF
    merger.write(os.path.join(os.path.dirname(__file__), "merged-pdf.pdf"))  # to write

    merger.close()
    print("PDFs merged successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
