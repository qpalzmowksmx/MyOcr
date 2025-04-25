# MyOcr

개인pdf 파일이 용량이 커서 구글 드러이브로 안돼서 해보는 프로그램

main.py --only text
image.py --이미지도 가능한 버전

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


하고싶은거
+---------------------+
|      Web App        |
+----------+-----------+
           |            
+----------v-----------+
|       Redis          |  <- 중간 데이터 저장(관리자데이터 확인 전까지 대기), 이미지 등 스캔한txt 데이터 저장
+----------+-----------+
           |
+----------v-----------+
|      MYSQL DB        |  <- 최종 정규화된 데이터 저장
+----------------------+

도커?등으로 해서
사용자가 영수증 올리면 그걸 redis가 가지고있다가
담장자가 실물 사진과 인식한 데이터가 맞으면 mysql에 반영
품목명과 사용자명 가격이 들어가고
인덱싱은 해당 영수증에 autoincrement 키를 부여해서
조회시 빠른 조회기능

해야할꺼
{
    영수증 서명-이미지로 따로 저장을 어케할지
    품목을 인식시킬때 미리 하나하나는 못하니까 범주를 선입력 해야하는데 어케할지
    품목을 인식시킬때 예외처리
    레디스? 일단 임시저장용이랑 최종용 2개 구동시 부하?
    다수의 이용자가 올릴때 누가 올렸는지 어떻게 구분할지
    선입선출 잘 되게 하기

    계속 생각나면 수정하기
}