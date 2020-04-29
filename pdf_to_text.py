try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pdf2image import convert_from_path

file_name = './pharmaceutical-development-con-clo-sys.pdf'
images = convert_from_path(file_name)
images[0].save('./page_1.jpg', 'JPEG')


print(pytesseract.image_to_string(Image.open('ocr.jpg')))
