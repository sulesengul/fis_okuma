import cv2
import pytesseract
from PIL import Image
import re

#pytesseract.pytesseract.tesseract_cmd = r"C:\Users\sules\Desktop\C\tesseract-main"


def ocr_text(image_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except FileNotFoundError:
        print(f"Dosya bulunamadı.")
        return None

if __name__ == "__main__":
    image_path = "/content/market-fis.jpg"
    extracted_text = ocr_text(image_path)
    if extracted_text:
       print("Resimden çıkarılan metin: ")
       print(extracted_text)
    pattern = r"alınan para .*"
    match = re.search(pattern, extracted_text, re.MULTILINE | re.IGNORECASE)
    if match:
        print("Toplam Tutar:", match.group())
    else:
        print("Toplam Tutar bulunamadı.")

