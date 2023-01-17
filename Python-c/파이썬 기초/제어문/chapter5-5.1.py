data = []

x = int(input("1일차 턱걸이 횟수>>>"))
data.append(x)
x = int(input("2일차 턱걸이 횟수>>>"))
data.append(x)
x = int(input("3일차 턱걸이 횟수>>>"))
data.append(x)
x = int(input("4일차 턱걸이 횟수>>>"))
data.append(x)
x = int(input("5일차 턱걸이 횟수>>>"))
data.append(x)
x = int(input("6일차 턱걸이 횟수>>>"))
data.append(x)
x = int(input("7일차 턱걸이 횟수>>>"))
data.append(x)

total = sum(data)
avg = total // 7

print(avg)