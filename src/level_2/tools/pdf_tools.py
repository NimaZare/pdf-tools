import os
from PyPDF2 import PdfReader, PdfMerger, PdfWriter


def extract_information(pdf_path):
    """
    Extract metadata and number of pages from a PDF file.
    """
    with open(pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        information = pdf.metadata
        number_of_pages = len(pdf.pages)

    txt = f"""\n\n
    Information about {pdf_path}:

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    \n\n"""

    print(txt)
    return information


def merge_pdfs(paths, output):
    """
    Merge multiple PDF files into a single PDF file.
    """
    merger = PdfMerger()

    for path in paths:
        merger.append(path)

    os.makedirs(os.path.dirname(output), exist_ok=True)

    merger.write(output)
    merger.close()

    print(f"Merged PDF saved as {output} successfully.")


def split_pdf(path, output_folder, page_numbers):
    """
    Split a PDF file into individual pages and save them as separate PDF files.
    """
    pdf = PdfReader(path)
    for page_num in page_numbers:
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page_num])

        output_path = f"{output_folder}/page_{page_num+1}.pdf"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

    
    print("\nAll pages splitted successfully.\n")
