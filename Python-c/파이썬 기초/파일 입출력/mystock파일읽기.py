import csv

# #파일 읽기
# file = open(".\실습\파일 입출력\student.csv", "r", encoding = "utf-8-sig")
# reader = csv.reader(file)
# for data in reader:
#     print(data)
# file.close()
def show_profit(data):
    name = data[0]
    purchase_price = int(data[1]) #매입가
    amount = int(data[2]) #수량
    target_price = int(data[3]) #목표가
        
    profit = (target_price - purchase_price)* amount
    profit_ratio = (target_price / purchase_price -1 )*100
    
    print(f"{name} {profit} {profit_ratio : .2f}%")
    
file = open(".\실습\파일 입출력\mystock.csv", "r", encoding="utf-8-sig")
reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data)
    # print(data)
file.close()