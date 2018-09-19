import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import platform
from matplotlib import font_manager, rc
from insert_XY import insertXY

import googlemaps
gmaps = googlemaps.Client(key='AIzaSyD6kbIPQKIcLsHLwAhttEQApCsUl0_3rIc')

# 자치단체 주차장 현황 data 삽입
park = pd.read_csv('./data/2018_parking_free_chu.csv')

# column name을 보기 편하게 변경
park.rename(columns={"주차장유형 (노상/노외/부설)":"주차장유형",
                  "전화번호 (주차장관리자)":"전화번호"}, inplace=True)


# 주차장명이 없는 CASE
row, col = park.shape
for i in range(row):
    # 주차장명이 float(nan) 인 경우 해당 row를 삭제
    if type(park['주차장명'][i]) == float:
        park.drop([i], inplace=True)


# 개방시작, 개방종료 시간 양식 통일화
# ex1) 0:00 -> 00:00
# ex2) 미개방 -> nan
for cols in park.keys():
    if '개방' in cols:
        for i in park.index:
            try:
                len(park[cols][i])
            except:
                1
            else:
                if len(park[cols][i]) == 4 and ':00' in park[cols][i]:
                    park[cols][i] = '0' + park[cols][i]
                elif '24:00' in park[cols][i]:
                    park[cols][i] = '24:00'
            print("num!", i)

# 개방시작시간, 개방종료시간 combine
# 14일 00:00, 24:00 -> 14,00:00~24:00
# day_flag(개방시작시간) == 0
# day_flag(개방종료시간) == 1
day_flag = 0
for cols in park.keys():
    # 개방시작시간 읽으면서 종료시간까지 읽고 combine하여 새로운 column 생성
    if '개방' in cols and day_flag == 0:
        day_flag = 1
        days, tmp = cols.split(', ')
        year, month, day_week = days.split('.')
        new_cols = month+'.'+day_week
        day, week = day_week.split('(')
        
        park[new_cols] = day + ',' + park[cols] + '~' + park[days+', 개방종료시간']
        park.rename(columns={cols:days}, inplace=True)
        
    elif day_flag == 1:
        day_flag = 0

# 기존의 날짜 column 삭제
for cols in park.keys():
    if "18" in cols or 'Unnamed' in cols:
        del park[cols]

# 위도가 비어있는 부분을 찾아 print하여 확인하는 작업
# print를 이제 dict에서 x, y에 저장해야 하지만 데이터를 못찾는 부분이 존재함
for i in park.index:
    try :
        addr_ll = gmaps.geocode(park['주소'][i], language='ko')[0]['geometry']['location']
        addr_x = str(addr_ll['lat'])
        addr_y = str(addr_ll['lng'])
    except :
        1
    finally:
        print(i, addr_x, addr_y, park.주차장명[i])
        park['위도'][i] = addr_x
        park['경도'][i] = addr_y

park.to_csv('./data/2018_chu_data_free.csv', encoding='utf-8-sig')
