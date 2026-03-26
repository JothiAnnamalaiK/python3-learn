from PyPDF2 import PdfWriter, PdfReader
import os

try:
    writer = PdfWriter()

    filepath = os.path.join(os.path.dirname(__file__), "compress-pdf")

    pdf_list = [
        os.path.join(filepath, f) for f in os.listdir(filepath) if f.endswith(".pdf")
    ]

    for pdf in pdf_list:
        # need to compress the all avail pdf one by one and replace the original pdf with the compressed one
        reader = PdfReader(pdf)

        for page in reader.pages:
            page.compress_content_streams()  # for compressing the content stream of each page # This is CPU intensive!
            writer.add_page(page)

        compressed_pdf_path = os.path.splitext(pdf)[0] + "_compressed.pdf"
        with open(compressed_pdf_path, "wb") as f:
            writer.write(f)
        writer = PdfWriter()  # Reinitialize the writer for the next file

        writer.close()
    print("PDFs compressed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
