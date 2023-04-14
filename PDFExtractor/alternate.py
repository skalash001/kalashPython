import PyPDF2

def remove_alternate_pages(file_path):
    start_page = int(input('Enter the page number to start removing alternate pages from: '))
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range(len(pdf_reader.pages)):
            if page_num < start_page or page_num % 2 == 0:
                pdf_writer.add_page(pdf_reader.pages[page_num])
        new_file_path = file_path.split('.pdf')[0] + '_new.pdf'
        with open(new_file_path, 'wb') as new_file:
            pdf_writer.write(new_file)
        print(f'New file saved at {new_file_path}')

remove_alternate_pages('C:\\Users\\skala\\OneDrive\\Documents\\BreeZip\\Kanvasatapathabrahmaaam_Vol_IV conv conv.pdf')

