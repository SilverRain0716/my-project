#with 구문으로 하면 close를 자동으로 해줌
with open(".\실습\파일 입출력\data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)
    