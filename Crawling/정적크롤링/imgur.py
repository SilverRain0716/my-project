# 이미지도 문자열이다.
# ASCII코드로 이루어져 있다.
# MIME를 같이 보냄

import requests as req

url = "https://api.imgur.com/3/image?client_id=546c25a59c58ad7"

# 첫번째 방법
# f = open("Crawling/네추럴메이드_비타민D_1.jpeg", "rb")
# img = f.read()

# 두번째 방법

with open("Crawling/네추럴메이드_비타민D_1.jpeg", "rb") as f:
    img = f.read()

f.close

# print(len(img))


res = req.post(url, files={
    "image": img,
    "type": "file",
    "name": "네추럴메이드_비타민D_1.jpeg"
})
# print(res.status_code)
# print(res.text)

link = res.json()["data"]["link"]
print(link)

html = f"""
<html>
<head>
    <title> 방금 업로드한 이미지 </title>
</head>
<body>
    <img src="{link}">
</body>
</html>
"""
with open("image.html", "w") as f:
    f.write(html)
