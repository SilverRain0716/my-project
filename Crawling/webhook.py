import requests as req

# get방식으로 요청
# res = req.get("https://webhook.site/2aca1086-5c43-4956-8e8a-9df265348ad6?name=hi",
#               headers={"User-Agent": "fastcampus/BI"})

# 포스트 방식으로 요청
url = "https://webhook.site/2aca1086-5c43-4956-8e8a-9df265348ad6"
res = req.post(url)

print(res.text)
