list = ["아버지", "어머니", "누나", "언니"]
score = 0
print("[낱말 맞추기]")

for word in list:
    print(word)
    data = input("입력>>>")
    if data == word:
        score += 1
print("전체 문제 수 : ", len(list))
print("맞힌 문제 수 : ", score)
print("틀린 문제 수 : ", len(list) - score)
