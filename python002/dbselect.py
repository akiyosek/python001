#!/usr/bin/env python3

import mysql.connector
import time

db_host='localhost'
db_name='test'
db_user='akiyosek'
db_pass='Druaga60#'
start = time.time()
conn = mysql.connector.connect(
                            user=db_user,
                            password=db_pass,
                            host=db_host,
                            database=db_name)
try:
    cur = conn.cursor()
    sql = "SELECT * FROM test"
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print(row)
        
finally:
    cur.close()
    conn.close()
elapsed_time = time.time() - start
print(elapsed_time)