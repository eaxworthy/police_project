import PyPDF2 as pf
import sys
import re

def read_pdf():

    #read in pdf
    in_file = input('Pdf Location: ')
    reader = pf.PdfFileReader(in_file)

    #get number of pages
    page_count = reader.numPages

    file_name_approved = False
    while not file_name_approved:
        output_file = input('Output file path: ') + '.txt'
        print('File will be written to '+ output_file)
        approval = ''
        while approval not in ['yes', 'no']:
            approval = input('Is this correct? (yes/no)').lower()
            if approval == 'yes':
                file_name_approved = True

    with open(output_file, 'w') as output:
            for i in range(page_count):
                page = reader.getPage(i)

                #pdf specific cleaning. change according to needs
                page = re.sub(r"(\d\d:\d\d)", r"\n\1", page.extractText())
                page = re.sub(r"\s\s+", " ", page)
                page = re.sub("\.\s\.", ".", page)
                if i==0:
                    newline = page.find('\n')
                    page = page[newline+2:]
                
                

                output.write(page)

    
read_pdf()
