import random


inputan=random.randint(1, 100)
if inputan < 1 or inputan >100:
    print("ya,malah di input juga, selesai deh")
else : 
    print(" nah gitu dong nurut")
    sisahasilbagi=inputan%2
    if sisahasilbagi==0:
        print(inputan," adalah bilangan genap")
    else:
        print(inputan,"adalah bilangan ganjil")
        