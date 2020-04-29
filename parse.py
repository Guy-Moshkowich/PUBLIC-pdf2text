from os import walk
import PyPDF2


f = '/Users/guymoshkowich/Downloads/yaron/32-body-data/32p-drug-prod/doxo-hcl-lipo-inj-inj/32p2-pharm-dev/pharmaceutical-development-con-clo-sys.pdf'
pdfFileObj = open(f, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
num_pages = pdfReader.numPages
for i in range(num_pages):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
exit(0)

pdf_list = []
for (dirpath, dirnames, filenames) in walk('../yaron'):
    pdf_delta = [dirpath + '/' + x for x in filenames if 'pdf' in x]
    if len(pdf_delta) > 0:
        pdf_list.extend(pdf_delta)

print(len(pdf_list))
for file in pdf_list:
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    for i in range(num_pages):
        pageObj = pdfReader.getPage(i)
        print(pageObj.extractText())

