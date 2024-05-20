import pymysql
import os

conn = pymysql.connect(
    host="localhost", user="encore", password="encore1234"
)

cur = conn.cursor(pymysql.cursors.DictCursor)

with open(r"C:\Users\USER\Downloads\employees\employees.sql", encoding="utf-8") as file:
    sql = file.read()

sql = sql.split(";")
# 리스트로 되어있음
# sql = """
# source C:\Users\USER\Downloads\employees\employees.sql
# """
for i in sql:
    try:
        print(cur.execute(i))
    except Exception as e:
        print(e)
        i.replace("\\", os.path.sep)

# result = cur.fetchall()

# print(result[0])


# mysql -u encore -p


# SELECT
# *
# FROM 'shopdb','memberID'
# WHERE 'memberID' = 'asdf';

# INSERT INTO
# 'membertbl' ('memberID', 'memberName','memberAddresss')
# VALUES('asdfb','홍길동','분당')
