input_korean = int(input("국어>>"))
input_math = int(input("수학>>"))
input_eng = int(input("영어>>"))
total = input_korean + input_math + input_eng
avg = total//3

if input_korean < 0 or input_math < 0 or input_eng < 0:
    print("잘못 입력하셨습니다.")
elif input_korean >100 or input_math > 100 or input_eng > 100:
    print("잘못 입력하셨습니다.")
elif avg >= 80:
    print("불합격")
else:
    print("합격")