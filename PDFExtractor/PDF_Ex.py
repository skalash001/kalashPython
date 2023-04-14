import fitz
import os

# Open the PDF file
pdf_file = fitz.open('C:\\Users\\skala\\Downloads\\Kanvasatapathabrahmaaam_Vol_VI.pdf')

# Get the number of pages in the PDF file
num_pages = pdf_file.page_count

# Prompt the user for a page number to extract
page_num = int(input(f"Enter a page number to extract (1-{num_pages}): ")) - 1

# Check if the page number is valid
if page_num < 0 or page_num >= num_pages:
    print(f"Invalid page number. Please enter a number between 1 and {num_pages}.")
else:
    # Extract the specific page
    page = pdf_file[page_num]

    # Generate a unique filename based on the page number
    filename = f"Page{page_num + 1}.pdf"

    # Save the extracted page to a new PDF file
    new_pdf = fitz.open()
    new_pdf.insert_pdf(pdf_file, from_page=page_num, to_page=page_num)
    new_pdf.save(os.path.join('G:\\PDF_Extractor\\Extracted', filename))
    new_pdf.close()

    # Close the files
    pdf_file.close()

    print(f"Page {page_num + 1} has been extracted and saved as {filename}.")
