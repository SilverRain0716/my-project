import pickle

#pickle파일로 저장
data = {
    "목표1" : "매일 팔굽혀 펴기 100회",
    "목표2" : "매일 코딩 공부 1시간"
}

file = open(".\실습\파일 입출력\data.pickle", "wb")
pickle.dump(data, file)
file.close()

#pickle 파일 파이썬으로 가져오기
file = open(".\실습\파일 입출력\data.pickle", "rb")
data = pickle.load(file)
print(data, end = "")
file.close()


