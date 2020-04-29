from pdf2image import convert_from_path
import os


def extract_images(folder_pdf, file_pdf):
    name = file_pdf.split('.')[0]
    folder_image = './data/' + name + '_images'
    if not os.path.exists(folder_image):
        os.makedirs(folder_image)

    images = convert_from_path(folder_pdf + '/' + file_pdf)
    for cnt, image in enumerate(images):
        image.save(folder_image + '/' + str(cnt) + '.jpg', 'JPEG')


if __name__ == '__main__':
    extract_images('.', 'pharmaceutical-development-con-clo-sys.pdf');

