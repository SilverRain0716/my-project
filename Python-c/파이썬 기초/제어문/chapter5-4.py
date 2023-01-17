animals = ["코끼리", "사자", "벼룩", "원숭이"]
empty = []

print(animals[2])
print(animals[-1])

animals.append("고라니")
print(animals)

animals[1] = "청개구리"
print(animals)

del animals[0]
print(animals)

print(animals[1:3])
print(animals[:])
print(animals[:3])
print(animals[1:])

animals.sort(reverse = True)
print(animals)
animals.sort()
print(animals)