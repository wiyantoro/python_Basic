import random
komp=random.randint(1, 11)
#print(komp)
saya=input("kecil atau besar:")
if komp<=9:
    hasil='kecil'
else:
    hasil='besar'
if saya==hasil:
    print("kamu menang")
else:
    print("kamu kalah")



 



