"""list = ["아버지", "어머니", "누나", "언니"]
i = 0
while True:
    print("제시어 : ", list[i])
    word = input("보이는 단어를 입력하세요>>")
    if word == list[i]:
        i += 1
    else:
        break
while문을 썼을 때 리스트를 넘어가게 되면 에러가 남"""

list = ["아버지", "어머니", "누나", "언니"]
print("[낱말 맞추기]")

for word in list:
    print(word)
    data = input("제시어를 입력하세요>>>")
    if data != word:
        breakd