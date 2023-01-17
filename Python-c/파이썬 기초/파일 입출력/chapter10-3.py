import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형돈", 5, 22]
]

file = open(".\실습\파일 입출력\student.csv", "w", newline = "", encoding = "utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)
    
file.close()

