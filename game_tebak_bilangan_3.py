

while True:
        inputan=int(input("masukan bilangan dari 2 s.d 10: "))
        if inputan < 2 or inputan >10:
            print("ya,malah di input juga, selesai deh")
        else : 
            print(" nah gitu dong nurut")
            sisahasilbagi=inputan%2
            if sisahasilbagi==0:
                print(inputan," adalah bilangan genap")
            else:
                print(inputan,"adalah bilangan ganjil")
                
    
