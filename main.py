from os import walk
import os
from pdf_to_jpeg import extract_images


pdf_list = []
for (dirpath, dirnames, filenames) in walk('../yaron'):
    pdf_delta = [dirpath + '/' + x for x in filenames if 'pdf' in x]
    if len(pdf_delta) > 0:
        pdf_list.extend(pdf_delta)

print('number of pdf files: ' + str(len(pdf_list)))
for pdf_path in pdf_list:
    folder, file = os.path.split(pdf_path)
    print('extracting: ' + file)
    extract_images(folder, file)

