#!/usr/bin/env python
# coding: utf-8

# In[40]:


# 라이브러리 로드
import csv
import pandas as pd
import requests

headers = {'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}


# In[39]:


# 종목번호와 상장사 이름을 stock_code와 stock_name으로 설정

stock_code = "023450"
stock_name = "동남합성"

# 종목 URL 만들기
URL = "https://finance.naver.com/item/sise_day.nhn?code=023450&page=1"

#URL = f"https://finance.naver.com/item/sise_day.nhn?code={stock_code}&page=1"  - 종목코드 변수 사용


# In[30]:


table = pd.read_html(requests.get(url,headers=headers).text, encoding='cp949')
len(table)  # table 길이 확인


# In[48]:


# table[0]과 table[1]을 확인하면 table[0]에 일별시세 정보가 있음
temp = table[0]


# In[54]:


# dropna를 통해 결측치가 들어있는 row를 제거
temp1 = temp.dropna() # 행을 기준으로 모두 결측치인 경우 제거. 옵션 값없이 temp.dropna()를 이용하여도 행을 기준으로 


# In[56]:


temp1


# In[58]:


temp1.to_csv('stock.csv',encoding='cp949')

