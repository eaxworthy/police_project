import PyPDF2 as pf
import sys
import re

def read_pdf():

    #read in pdf
    pdf_folder = "original_logs/"
    in_file = input('Pdf Name: ')
    reader = pf.PdfFileReader(pdf_folder+in_file)

    #get number of pages
    page_count = reader.numPages

    output_file = "converted_logs/text_files/" + in_file[:-3] + 'txt'

    with open(output_file, 'w') as output:
            for i in range(page_count):
                page = reader.getPage(i)

                #pdf specific cleaning. change according to needs
                page = re.sub(r"(\d\d:\d\d)", r"\n\1", page.extractText())
                page = re.sub(r"\s\s+", " ", page)
                page = re.sub("\.\s\.", ".", page)
                
                output.write(page[130:]+'\n')

    
read_pdf()
