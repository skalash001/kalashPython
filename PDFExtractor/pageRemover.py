import os
import random
import string
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfReader, PdfWriter

input_path = input("Enter the path of the input PDF file: ")
start_page = int(input("Enter the starting page number: "))
end_page = int(input("Enter the ending page number: "))

# Generate a random name for the output file
output_name = input("What is the name of the Output file - ")
output_path = os.path.join(os.path.dirname(input_path), output_name)

with open(input_path, "rb") as input_file, open(output_path, "wb") as output_file:
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    for page_number in range(start_page - 1, end_page):
        page = pdf_reader.pages[page_number]
        pdf_writer.add_page(page)

    pdf_writer.write(output_file)

print(f"Modified PDF saved as '{output_name}' in the same directory as the input file.")
