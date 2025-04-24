# MyOcr

개인pdf 파일이 용량이 커서 구글 드러이브로 안돼서 해보는 프로그램

선행작업
라이브러리를 쓰기에
pip install pytesseract pdfplumber Pillow
이후 시작하기

파일을 지정하면 읽고 txt로 현 코드가 있는 디렉토리에 저장함

파일을 지정하면 읽는 동안 아래처럼 뜨다가 완료됩니다.
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
CropBox missing from /Page, defaulting to MediaBox
Text extracted to output.txt

drm 안걸린 600페이지 정도 되는 파일이 m4-pro-48gb 기준 1분 조금 넘네요.
빠르지는 않습니다.
C로 짰으면 빨랐겠지만 제가 C를 몰라요.
공부하는것으로 해야겠네요.

윈도우는 인터넷 검색해서 tesseract 설치

맥/리눅스는 명령어로
brew install tesseract
sudo apt-get install tesseract-ocr
등이요.
