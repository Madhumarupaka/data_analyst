from mysql.connector import connection



conn=connection.MySQLConnection(host="localhost",user="root",database="sakila",
                                password="Shreyan@422"
                                )
cursor=conn.cursor()
query="select price,rating from film_list where FID=15"
cursor.execute(query)
for x in cursor:
    print(x)
cursor.close()
conn.close()

