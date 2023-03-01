import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',    
    password='',
    database='latihan'
    )
print("welcome")
    
kunci=int(input("Id mana yang akan di hapus:"))

cursor=mydb.cursor() 
sql_query="delete from user where iduser='"+str(kunci)+"'"

print(sql_query)
print("data berasil di hapus")
cursor.execute(sql_query)
mydb.commit()
mydb.close()
            
                             