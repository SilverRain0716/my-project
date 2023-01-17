#람다 함수

def minus_one(a):
    return a -1

lambda a : a-1

#호출
print((lambda a: a-1)(10))

#변수로 호출
minus_one_2 = lambda a: a-1
print(minus_one_2(100))

#함수 2 
def is_positive_number(a):
    if a > 0:
        return True
    else:
        return False
    
#람다 2
lambda a : True if a > 0 else False

#람다 호출
print((lambda a :True if a > 0 else False)(-2))

is_positive_number = lambda a :True if a > 0 else False

print(is_positive_number(2))