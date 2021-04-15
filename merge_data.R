#라이브러리 불러오기 
library(gapminder)
library(dplyr)
library(ggplot2)
library(gridExtra)


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

# 데이터 합치기 

data123 <- rbind(dongnam,seoul, snk)
View(data123)

data123$num <- sequence(rle(data123$stock_name)$lengths)

str(data123)


# 합친 시계열 그래프

ggplot(data123, aes(x=num, y=closing_price, group=stock_name, colour=stock_name)) + geom_line() + ggtitle("배당일 기준 한달 전후의 주가 변동")+ geom_vline(xintercept = data123$num[22], color="green")+ geom_vline(xintercept = data123$num[64], color="blue")
+geom_vline(xintercept = data123$num[106], color="red")


#------------------ 개별 그래프 ------------------------
# 동남합성 
dong_plot <- ggplot(dongnam, aes(x=date, y=closing_price)) + geom_line() + ggtitle("동남합성 주가 변동")+ geom_vline(xintercept = as.numeric(dongnam$date[22]), color="green") # 배당 기준일 세로선 추가 

# 서울가스
gas_plot <- ggplot(seoul, aes(x=date, y=closing_price)) + geom_line() + ggtitle("서울가스 주가 변동")+ geom_vline(xintercept = as.numeric(seoul$date[22]), color="red")

# SNK
SNK_plot <- ggplot(snk, aes(x=date, y=closing_price)) + geom_line() + ggtitle("SNK 주가 변동")+ geom_vline(xintercept = as.numeric(snk$date[23]), color="red")


grid.arrange(dong_plot,gas_plot,SNK_plot,nrow=2, ncol=2)

