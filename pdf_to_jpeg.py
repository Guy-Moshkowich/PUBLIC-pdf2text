
from pdf2image import convert_from_path
import os

file_name = 'pharmaceutical-development-con-clo-sys.pdf'
pdf_name = file_name.split('.')[0]
folder_image = pdf_name + '_images'

os.mkdir(folder_image)
os.mkdir(folder_text)

images = convert_from_path(file_name)
for cnt, image in enumerate(images):
    image.save(folder_image + '/' + str(cnt) + '.jpg', 'JPEG')


