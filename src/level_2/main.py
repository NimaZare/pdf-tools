from tools.pdf_tools import (
    extract_information,
    merge_pdfs,
    split_pdf
)


def show_file_information():
    path = input("Enter the path to a PDF file (show file metadata): ").strip().replace('\\', '/').strip('"')
    try:
        extract_information(path)
    except Exception as e:
        print(f"[ERROR](show_file_information)--> {e}")

def tool_merge_pdfs():
    paths = []
    while True:
        path = input("Enter the path to a PDF file (or 'done' to finish): ").strip().replace('\\', '/').strip('"')
        if path.lower() == 'done':
            break
        paths.append(path)

    try:
        merge_pdfs(paths, output='src/level_2/output/merged.pdf')
    except Exception as e:
        print(f"[ERROR](merge_pdfs)--> {e}")

def tool_split_pdf():
    path = input("Enter the path to a PDF file to split: ").strip().replace('\\', '/').strip('"')
    output_folder = input("Enter the output folder for split pages: ").strip().replace('\\', '/').strip('"')
    page_numbers_input = input("Enter the page numbers to split (comma-separated, e.g., 1,3,5): ").strip()
    try:
        page_numbers = [int(num) - 1 for num in page_numbers_input.split(',')]
        split_pdf(path, output_folder, page_numbers)
    except Exception as e:
        print(f"[ERROR](split_pdf)--> {e}")

def main():
    while True:
        print("\n********** PDF Tools **********\n")
        print("1. Show PDF file information")
        print("2. Merge PDF files")
        print("3. Split PDF file")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            show_file_information()
        elif choice == '2':
            tool_merge_pdfs()
        elif choice == '3':
            tool_split_pdf()
        elif choice == '4':
            print("\n++++++++++++ Exiting the program ++++++++++++")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
