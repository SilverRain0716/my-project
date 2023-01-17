#실습 문제
import csv

data = [
    ["종목", "매입가", "수량", "목표가"],
    ["삼성전자", 85000, 10, 90000],
    ["네이버", 380000, 5, 400000],
]

file = open(".\실습\파일 입출력\mystock.csv", "w", newline = "", encoding = "utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()
