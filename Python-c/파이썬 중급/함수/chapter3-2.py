# map, filter 함수

print(list(map(int,['3', '4', '5', '6'])))

#리스트 모든 요소 공백

items = [' 로지텍 마우스 ', ' 앱솔키보드 ']

# for 사용
for i in range(len(items)):
    items[i] = items[i].strip()
print(items)

# 람다 함수 

items = list(map(lambda x : x.strip(), items))
print(items)


# 필터 함수
def func(x):
    return x < 0
print(list(filter(func, [-3,-2,0,5,7])))

animalls = ['cat', 'tiger', 'dog', 'bird', 'money']
result = []
for i in animalls:
    if len(i) <= 3:
        result.append(i)
print(result)

def word_check(x):
    return len(x) <=3

result = list(filter(word_check, animalls))
print(result)

result = list(filter(lambda x : len(x) <= 3, animalls))
print(result)