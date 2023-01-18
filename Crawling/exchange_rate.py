import requests as req
import re

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text

#r = re.compile(r"미국 USD.*?value\">(.*?)</", re.DOTALL)
r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)

captures = r.findall(body)

print("--------")
print("환율 보기")
print("--------")
print("")

for c in captures:
    print(c[0] + " : " + c[1])
    
print()

usd = float(captures[0][1].replace(",","")) 
# 위에서 리스트 첫번째 값 안에서 2번째 값을 가져온다.
# 콤마(,)를 없애준다. 
won = input("원화를 입력하세요>>>")
won = int(won)
while True:
    if won >= 10000: 
        dollor = won / usd
        dollor = int(dollor)
        print(f"{dollor} 달러 환전되었습니다.")
        break
    else:
        won = input('다시 입력하세요>>')
        won = int(won)
       
    
    # else:
    #     if won < 9999:
    #         won = input('다시 입력하세요>>')
    #         won = int(won)
    #     else:
    #         print(f"{dollor} 달러 환전되었습니다.")    