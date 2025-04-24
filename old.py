import pytesseract
from pdfplumber import open as open_pdf
from PIL import Image
import asyncio
import os


# Tesseract 경로 설정
# 윈도우에서 pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# MacOS에서 Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

async def extract_text_from_pdf(pdf_path, output_txt_path):
    import asyncio

    with open_pdf(pdf_path) as pdf:
        text_content = []
        
        for page in pdf.pages:
            # 페이지의 텍스트를 추출
            text = page.extract_text()
            if text:
                text_content.append(text)
            else:
                # OCR이 필요한 경우 이미지를 처리
                img = await page.to_image()
                ocr_result = pytesseract.image_to_string(img)
                text_content.append(ocr_result)

    # 추출된 텍스트를 txt 파일에 저장
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(text_content))

# 비동기 함수 실행
pdf_file_path = 'local_file.pdf'  # 로컬 PDF 경로
output_text_file = 'output.txt'   # 출력 텍스트 파일

asyncio.run(extract_text_from_pdf(pdf_file_path, output_text_file))


# def extract_text_from_pdf(pdf_path, output_txt_path):
#     with open_pdf(pdf_path) as pdf:
#         text_content = []
        
#         for page in pdf.pages:
#             # 페이지의 텍스트를 추출
#             text = page.extract_text()
#             if text:
#                 text_content.append(text)
#             else:
#                 # OCR이 필요한 경우 이미지를 처리
#                 with page.to_image() as img:
#                     ocr_result = pytesseract.image_to_string(img)
#                     text_content.append(ocr_result)

#     # 추출된 텍스트를 txt 파일에 저장
#     with open(output_txt_path, 'w', encoding='utf-8') as f:
#         f.write('\n\n'.join(text_content))

# # 사용 예시
# pdf_file_path = 'local_file.pdf'  # 로컬 PDF 경로
# output_text_file = 'output.txt'   # 출력 텍스트 파일

# extract_text_from_pdf(pdf_file_path, output_text_file)
