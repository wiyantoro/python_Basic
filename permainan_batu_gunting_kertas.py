import random

print("permainan batu,gunting,kertas")
print("1.batu")
print("2.gunting")
print("3.kertas")
nilai=random.randint(1,3)
tebak=int(input("tekan 1.batu,tekan 2.gunting,tekan 3.kertas:"))
#batu
if nilai ==1 and tebak==1:
    print("seri")
else:
    if nilai==1 and tebak==2:
        print("komputer batu, kamu kertas (menang)")
    else:
        if nilai==1 and tebak ==3:
            print("komputer batu, kamu kertas(menang)")
        else:
            #gunting
            if nilai ==2 and tebak==1:
                print("komputer gunting,kamu batu(menang)")
            else:
                if nilai==2 and tebak==2:
                    print("seri")
                else:
                    if nilai==2 and tebak ==3:
                        print("komputer gunting(menang), kamu kertas")
                        #kertas
                    else:
                            if nilai ==3 and tebak==1:
                                print("komputer kertas(menang),kamu batu")
                            else:
                                if nilai==3 and tebak==2:
                                    print("komputer kertas,kamu guntung(menang)")
                                else:
                                    if nilai==3 and tebak ==3:
                                        print("seri")
                        
 