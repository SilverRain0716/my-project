input_time = int(input("공부시간을 입력하세요>>>"))

if input_time >= 10:
    print("휴대폰 잠금이 해제 됩니다.")
elif input_time < 10 and input_time >= 5:
    print("휴대폰을 30분간 사용가능 합니다.")
else:
    print("휴대폰 사용이 불가능합니다.")