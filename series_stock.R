#라이브러리 불러오기 
library(gapminder)
library(dplyr)
library(ggplot2)


# 전처리된 csv 파일 불러오기 
dongnam <- read.csv(file = "cut_stock_1.csv")
seoul <- read.csv(file = "cut_stock_2.csv")
snk <- read.csv(file = "cut_stock_3.csv")

# 파일 구조 확인 및 데이터 내용 확인
str(dongnam)
str(seoul)
str(snk)

head(dongnam)
head(seoul)
head(snk)

# date의 데이터타입 변환
dongnam$date <- as.Date(dongnam$date)
seoul$date <- as.Date(seoul$date)
snk$date <- as.Date(snk$date)

# 시계열 그래프

# 동남합성
ggplot(dongnam, aes(x=date, y=closing_price)) 
+ geom_line() + ggtitle("동남합성 주가 변동")
+ geom_vline(xintercept = as.numeric(dongnam$date[22]), color="red") # 배당 기준일 세로선 추가

# 서울가스
ggplot(seoul, aes(x=date, y=closing_price)) 
+ geom_line() + ggtitle("서울가스 주가 변동")
+ geom_vline(xintercept = as.numeric(seoul$date[22]), color="red")

# SNK
ggplot(snk, aes(x=date, y=closing_price)) 
+ geom_line() + ggtitle("SNK 주가 변동")
+ geom_vline(xintercept = as.numeric(snk$date[23]), color="red")