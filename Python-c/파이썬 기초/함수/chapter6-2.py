#로또 번호 뽑기
import random

"""
반복문, 조건문, 리스트를 이용해서 알고리즘 구현, 함수사용
"""
def get_random_number():
    number = random.randint(1, 45)
    return number

lotto_num = []
count = 0 #현재 뽑은 숫자 개수

while True:
    if count > 5:
        break
    random_number = get_random_number()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1
    
lotto_num.sort()
for num in lotto_num:
    print(num, end = " ")
    