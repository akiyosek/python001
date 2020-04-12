# -*- coding: utf-8 -*-
import mysql.connector as mydb

# コネクション作成
conn = mydb.connect(
    host='localhost',
    port='3306',
    user='akiyosek',
    password='Druaga60#',
    database='test'
)

# DB操作用にカーソルを作成
cur = conn.cursor()


# データ投入
cur.execute("INSERT INTO test VALUES (1, 'scott', '1件目のデータ', '2020/04/12')")

# DB操作が終わったらカーソルとコネクションを閉じる
cur.close()
conn.close()