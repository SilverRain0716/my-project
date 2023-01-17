#모듈 추가
import sqlite3

#db열기
conn = sqlite3.connect(r"C:\Users\ha_wongbi\Documents\GitHub\fastcamp\파이썬 중급\데이터베이스\1.db")

cur = conn.cursor()

INSERT_SQL = "INSERT INTO item(code, name, price) VALUES(?,?,?)"

# 연결
cur.execute(INSERT_SQL, ('A00001', '게이밍 마우스', 30000))

# 커밋
conn.commit

# 데이터 베이스 닫기
conn.close()