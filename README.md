# 각 자치단체, 교육청에서는 명절마다 주차장을 무료로 개방합니다.이것을 홍보하고 국민들에게 많이 알리고자 웹페이지를 만들었습니다.
# 주차장 데이터를 공공데이터포털 에서 제공받아 전처리를 해주는 코드입니다.

## 실행 파일으로는 Read_data.py 입니다.

### 사용 언어는 파이썬입니다. data 폴더에 2018년 설 자치단체 주차장 data와 교육청 주차장 data가 첨부되어 있습니다. 전처리 내용으로는 각 column 명을 사용하기 편하도록 변경하였고 날짜를 사용하기 편하도록 변경하였으며 각 주차장의 위, 경도가 비어있는 부분이 있습니다. 비어있는 부분을 naver map api, googlemaps api를 사용하여 빈 데이터를 채웠고 잘못 입력되어있는 데이터를 식별하여 사전에 삭제하는 방법을 채택했습니다. 등등의 여러가지 들은 코드 안의 주석부분을 확인해주시기 바랍니다.

## 자세한 내용, 궁금한 내용은 rjsdn315@gmail.com 으로 메일 보내주시면 답변해드리겠습니다.

## ※ 참고     https://github.com/rjsdn31536/publicparking   웹페이지 구동 코드는 참고 github을 참고하시기 바랍니다.
