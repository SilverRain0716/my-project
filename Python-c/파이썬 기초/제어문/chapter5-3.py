input_money = int(input("현재 가진 금액을 입력하세요>>"))
basic = "오늘 저녁은..."

if input_money >= 20000:
    print(basic + "치킨")
elif input_money >= 10000:
    print(basic + "떡볶이")
elif input_money >= 2000:
    print(basic + "편의점 김밥")
else:
    print(basic + "굶어야해...")