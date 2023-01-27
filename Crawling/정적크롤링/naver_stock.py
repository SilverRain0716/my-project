from bs4 import BeautifulSoup as BS
import requests as req

url = "https://finance.naver.com/sise/lastsearch2.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

for tr in soup.select("table.type_5 tr"):
    if len(tr.select("a.tltle")) == 0:
        continue
    title = tr.select("a.tltle")[0].get_text(strip=True)
    print(title)
