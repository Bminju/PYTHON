#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 라이브러리 로드
import csv
import pandas as pd
import requests

headers = {'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}


# In[2]:


# 종목번호와 상장사 이름을 stock_code와 stock_name으로 설정

stock_code = "950180"
stock_name = "SNK"

# 종목 URL 만들기 - table 길이 확인, 정보의 위치 확인을 위해 1page 정보 
url = f"https://finance.naver.com/item/sise_day.nhn?code=950180&page=1" #URL = f"https://finance.naver.com/item/sise_day.nhn?code={stock_code}&page=1"  - 종목코드 변수 사용
html = requests.get(f"https://finance.naver.com/item/sise_day.nhn?code=950180&page=1")  
table = pd.read_html(requests.get(url,headers=headers).text, encoding='cp949') 


# In[3]:


len(table)  # table 길이 확인


# In[4]:


# table[0]과 table[1]을 확인하면 table[0]에 일별시세 정보가 있음
data = table[0]  
data  # data 확인과 결측치 확인


# In[6]:


# 원하는 날짜의 시가가 page 확인 후 for문 범위 설정. 
i = 0    # i = 0 으로 초기화 꼭 해줘야함
for i in range(18, 24):
    url = f"https://finance.naver.com/item/sise_day.nhn?code=950180&page={i}"
    html = requests.get(f"https://finance.naver.com/item/sise_day.nhn?code=950180&page={i}")  
    table = pd.read_html(requests.get(url,headers=headers).text, encoding='cp949') 
    if i == 18:
        data = table[0].dropna()  # 첫페이지의 경우 data 병합이 필요없으므로 결측치 제거만 해줌
    else:
        data1 = table[0].dropna()  # 두번째 페이지부터 결측치 제거와 병합실행
        data = pd.concat([data, data1])
# data = data.reset_index(drop = True)


# In[7]:


data = data.reset_index(drop=True) # 인덱스 넘버 재정렬
data


# In[8]:


data.to_csv('stock_3.csv',encoding='cp949')  # csv 파일로 저장


# In[ ]:


print(data)

