# from mysql.connector import connection
# conn=connection.MySQLConnection(host="localhost",database="world",user="root",password="Shreyan@422")
# cursor=conn.cursor()
# query="select * from city where id=5"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# cursor.close()
# conn.close()

from mysql.connector import connection
conn=connection.MySQLConnection(host="localhost",database="world",user="root",password="Shreyan@422")
cursor=conn.cursor()
query="select * from city where ID=15"
cursor.execute(query)
for x in cursor:
    print(x)
cursor.close()
conn.close()