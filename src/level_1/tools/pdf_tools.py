from PyPDF2 import PdfReader, PdfMerger

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

    merger.write(output)
    merger.close()

    print(f"Merged PDF saved as {output} successfully.")

