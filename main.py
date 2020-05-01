from os import walk
import os
from pdf_to_images import extract_doc_images
from image_to_text import extract_doc_text

pdf_list = []
for (dirpath, dirnames, filenames) in walk('data/m3'):
    pdf_delta = [dirpath + '/' + x for x in filenames if 'pdf' in x]
    if len(pdf_delta) > 0:
        pdf_list.extend(pdf_delta)

print('number of pdf files: ' + str(len(pdf_list)))
for pdf_path in pdf_list:
    print('extracting: ' + pdf_path)
    extract_doc_images(pdf_path)

for doc_images_folder in os.listdir('./data/images'):
    print(doc_images_folder)
    extract_doc_text('./data/images/' + doc_images_folder)