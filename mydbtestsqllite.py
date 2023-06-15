import sqlite3
conn=sqlite3.connect('mynewsql.db')
cur=conn.cursor()
cur.execute("INSERT INTO STUDENT VALUES(2,'SUNNY')")
conn.commit()