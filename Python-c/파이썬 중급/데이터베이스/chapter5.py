#모듈 추가
import sqlite3

#db열기
conn = sqlite3.connect("./1.db")

cur = conn.cursor()

CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS Item(
        id integer primary key autoincrement,
        code text not null,
        name text not null,
        price integer not null
    )
"""
# 연결
cur.execute(CREATE_SQL)

# 데이터 베이스 닫기
conn.close()