
import random

print("permainan batu,gunting,kertas")
print("1.batu")
print("2.gunting")
print("3.kertas")

tebak=int(input("tekan 1.batu,tekan 2.gunting,tekan 3.kertas:"))
#batu
scorecomp=0
scoreman=0
for i in range(1,4):
    print('suit')
    nilai=random.randint(1,3)
        if nilai ==1 and tebak==1:
            print("seri")
        else:
            if nilai==1 and tebak==2:
                print("komputer batu, kamu kertas (menang)")
                scoreman+=1
            else:
                if nilai==1 and tebak ==3:
                    print("komputer batu, kamu kertas(menang)")
                    scoreman+=1
                else:
                    #gunting
                    if nilai ==2 and tebak==1:
                        print("komputer gunting,kamu batu(menang)")
                        scoreman+=1
                    else:
                        if nilai==2 and tebak==2:
                            print("seri")
                        else:
                            if nilai==2 and tebak ==3:
                                print("komputer gunting(menang), kamu kertas")
                                scorecomp+=1
                                #kertas
                            else:
                                    if nilai ==3 and tebak==1:
                                        print("komputer kertas(menang),kamu batu")
                                        scorecomp+=1
                                    else:
                                        if nilai==3 and tebak==2:
                                            print("komputer kertas,kamu guntung(menang)")
                                            scoreman+=1
                                        else:
                                            if nilai==3 and tebak ==3:
                                                print("seri")
 print('score komp sementara:', scorecomp)
 print('score sementara manusia:', scoreman)
 
if scorecomp==scoreman:
    print("hasil seri")
else:
    if scorecomp>scoreman:
        print("komputer menang")
    else:
     topscorename=input("siapa nama anda")
     file = open('C:/wiyan/sesi_2/nila.txt') 
    
    
 