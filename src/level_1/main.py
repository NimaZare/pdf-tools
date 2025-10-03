import src.level_1.tools.pdf_tools as pdf_tools


def show_file_information():
    path = input("Enter the path to a PDF file (show file metadata): ").strip()
    try:
        pdf_tools.extract_information(path)
    except Exception as e:
        print(f"[ERROR](show_file_information)--> {e}")

def merge_pdfs():
    paths = []
    while True:
        path = input("Enter the path to a PDF file (or 'done' to finish): ")
        if path.lower() == 'done':
            break
        paths.append(path)

    try:
        pdf_tools.merge_pdfs(paths, output='src/level_1/assets/merged.pdf')
    except Exception as e:
        print(f"[ERROR](merge_pdfs)--> {e}")

def main():
    while True:
        print("\n********** PDF Tools **********\n")
        print("1. Show PDF file information")
        print("2. Merge PDF files")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            show_file_information()
        elif choice == '2':
            merge_pdfs()
        elif choice == '3':
            print("\n++++++++++++ Exiting the program ++++++++++++")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
