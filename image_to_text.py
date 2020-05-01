from PIL import Image
import pytesseract
from os import listdir
import os


def extract_doc_text(images_folder):
    base, doc_name = os.path.split(images_folder)
    text_folder = './data/text/' + doc_name
    if not os.path.exists(text_folder):
        os.makedirs(text_folder)
        for file_name in listdir(images_folder):
            if not '.jpg' in file_name:
                continue
            base, page_file = os.path.split(file_name)
            text = pytesseract.image_to_string(Image.open(images_folder + '/' + page_file))
            page = page_file.split('.')[0]
            text_path = text_folder + '/' + page + '.txt'
            text_file = open(text_path, 'w')
            text_file.write(text)
            text_file.close()


