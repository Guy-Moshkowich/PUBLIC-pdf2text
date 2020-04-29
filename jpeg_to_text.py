from PIL import Image
import pytesseract
from os import listdir


image_folder = 'pharmaceutical-development-con-clo-sys_images'
text_folder = image_folder.split('_')[0] + '_text'
for file_name in listdir(image_folder):
    text = pytesseract.image_to_string(Image.open(image_folder + '/' + file_name))
    text_path = text_folder + '/' + file_name.split('.')[0] + '.txt'
    text_file = open(text_path, 'w')
    text_file.write(text)
    text_file.close()
    print(text)
