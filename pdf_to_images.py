from pdf2image import convert_from_path
import os


def extract_doc_images(pdf_path):
    name = pdf_path.replace('/', '_')
    folder_image = './data/images/' + name
    if not os.path.exists(folder_image):
        os.makedirs(folder_image)
        images = convert_from_path(pdf_path)
        for cnt, image in enumerate(images):
            image.save(folder_image + '/' + str(cnt) + '.jpg', 'JPEG')


