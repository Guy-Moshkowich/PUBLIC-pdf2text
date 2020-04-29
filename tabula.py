import PyPDF2
f = '/Users/guymoshkowich/Downloads/yaron/32-body-data/32p-drug-prod/doxo-hcl-lipo-inj-inj/32p2-pharm-dev/pharmaceutical-development-con-clo-sys.pdf'
# import packages
import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader(f)

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "Hydrochloride"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i))
    Text = PageObj.extractText()
    # print(Text)
    ResSearch = re.search(String, Text)
    print(ResSearch)