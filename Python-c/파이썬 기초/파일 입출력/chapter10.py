
#파일 쓰기
file = open(r".\실습\파일 입출력\data.txt", "w", encoding="utf8")
file.write("1. 코딩공부")
file.close()

#파일 추가
file = open(r".\실습\파일 입출력\data.txt", "a", encoding="utf8")
file.write("\n2. 쉽다")
file.close()

#파일 읽기
file = open(".\실습\파일 입출력\data.txt", "r", encoding="utf8")

#파일 전체읽기
data = file.read()
print(data)
file.close()

#파일 한 줄 읽기
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()

