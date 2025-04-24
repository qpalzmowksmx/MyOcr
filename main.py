import pytesseract
from pdfplumber import open as open_pdf
from PIL import Image
import asyncio
from tkinter import Tk, filedialog

# MacOS에서 Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

async def extract_text_from_pdf(pdf_path, output_txt_path):
    try:
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
    except Exception as e:
        print(f"Error during PDF processing: {e}")

def select_file():
    # Tkinter의 root 창을 숨기고 파일 선택 대화 상자뜨게
    root = Tk()
    root.withdraw()  # Tkinter 창을 안뜨게 하는거

    pdf_file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if pdf_file_path:
        output_text_file = 'output.txt'
        asyncio.run(extract_text_from_pdf(pdf_file_path, output_text_file))
        print(f"Text extracted to {output_text_file}")
    else:
        print("No file selected.")

# 파일 선택 및 텍스트 추출
select_file()
