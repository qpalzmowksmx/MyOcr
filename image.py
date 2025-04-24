import pytesseract
from pdfplumber import open as open_pdf
from PIL import Image, ImageDraw
import asyncio
from tkinter import Tk, filedialog

# MacOS에서 Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

async def extract_text_from_pdf(pdf_path, output_txt_path, image_output_dir):
    try:
        with open_pdf(pdf_path) as pdf:
            text_content = []
            
            for i, page in enumerate(pdf.pages):
                # 페이지의 텍스트를 추출
                text = page.extract_text()
                if text:
                    text_content.append(text)
                
                # 이미지 파일로 저장 (옵션으로)
                image_path = f"{image_output_dir}/page_{i+1}.png"
                await save_page_as_image(page, image_path)

                if not text:
                    # OCR이 필요한 경우 이미지를 처리
                    img = await page.to_image()
                    ocr_result = pytesseract.image_to_string(img)
                    text_content.append(ocr_result)

        # 추출된 텍스트를 txt 파일에 저장
        with open(output_txt_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(text_content))
    except Exception as e:
        print(f"Error during PDF processing: {e}")

async def save_page_as_image(page, image_path):
    # 페이지를 이미지로 변환
    with open(image_path, 'wb') as f:
        pil_image = page.to_pil()
        pil_image.save(f, "PNG")

def select_file():
    root = Tk()
    root.withdraw()  # Tkinter 창 안뜨게

    pdf_file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if pdf_file_path:
        output_text_file = 'output.txt'
        image_output_dir = './images'  # 이미지를 저장할 디렉토리
        asyncio.run(extract_text_from_pdf(pdf_file_path, output_text_file, image_output_dir))
        print(f"Text extracted to {output_text_file} and images saved in {image_output_dir}")
    else:
        print("No file selected.")

# 파일 선택 및 텍스트 추출 실행
select_file()
