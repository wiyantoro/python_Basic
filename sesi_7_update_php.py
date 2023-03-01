import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',    
    password='',
    database='latihan'
    )
print("welcome")
    
kunci=int(input("Id mana yang akan diganti update:"))
userbaru=input("nama user:")
passbaru=input("Password:")
cursor=mydb.cursor() 
sql_query="update user set username='"+userbaru+"',password='"+passbaru+"' where iduser+'"+str(kunci)+"'"
cursor.execute("""
       UPDATE user
       SET username=%s, password=%s
       WHERE iduser=%s
       """,(userbaru,passbaru,kunci))
print(sql_query)
print("data berasil di update")
cursor.execute(sql_query)
mydb.commit()
mydb.close()
            
                             