import PyPDF2

# Open the PDF file in read-binary mode
with open('G:\PDF_Extractor\AAGAURPANI.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = pdf_reader.getNumPages()

    # Prompt the user for a page number to extract
    page_num = int(input(f"Enter a page number to extract (1-{num_pages}): ")) - 1

    # Check if the page number is valid
    if page_num < 0 or page_num >= num_pages:
        print(f"Invalid page number. Please enter a number between 1 and {num_pages}.")
    else:
        # Get the specific page from the PDF file
        page = pdf_reader.getPage(page_num)

        # Create a new PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()

        # Add the specific page to the new PDF writer object
        pdf_writer.addPage(page)

        # Generate a unique filename for the extracted page
        filename = f'page_{page_num + 1}.pdf'

        # Save the new PDF writer object as a new PDF file with a unique filename
        with open(f'G:\PDF_Extractor\{filename}', 'wb') as new_pdf_file:
            pdf_writer.write(new_pdf_file)

        print(f"Page {page_num + 1} has been extracted to a new PDF file with filename {filename}.")
