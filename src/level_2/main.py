import tools.read_write_pdf as pdf_tools


if __name__ == '__main__':
    path = 'src/level_1/assets/ResumeNimaZare_Python.pdf'
    pdf_tools.extract_information(path)

    paths = ['src/level_2/assets/ResumeNimaZare_C#.pdf', 'src/level_2/assets/ResumeNimaZare_Python.pdf']
    pdf_tools.merge_pdfs(paths, output='src/level_2/assets/merged.pdf')

