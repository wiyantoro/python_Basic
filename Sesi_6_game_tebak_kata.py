#Game Tebak Kata
import random

print("Permainan Tebak Kata")
with open ("C:/wiyan/sesi_2/sesi_6_tebak_kata.txt", 'r') as fp:
    lines =len(fp.readlines())
    print('Total Number of Lines' , lines)
if (lines>0):
    nilairand=random.randint(1,lines)
    file = open('C:/wiyan/sesi_2/sesi_6_tebak_kata.txt')
    content = file.readlines()
    hint1=content[nilairand-1]
    with open("C:/wiyan/sesi_2/sesi_6_tebak_kata.txt", 'r') as fp1:
        data=fp1.read()
        if(data!=""):
            print("Top Score saata ini: ", data)
        else:
            print("Belum ada Tope Score")

print("petunjuk:")
hint1=hint1.split(',')
print(hint1[0])
katatebak=hint1[1].replace('\n','')
jumlahhuruf=len(katatebak)
print("kata yang ditebak ada:", jumlahhuruf, "huruf")
benar=0
print("anda memiliki kesempatan",jumlahhuruf,"mencoba")
for i in range(jumlahhuruf):
    cobatebak=input("tebak ke "+str(i+1)+":")
    cobatebak=cobatebak.lower()
    
    if (katatebak==cobatebak):
        print("anda berasil menebak")
        if(i==0):
            topscorename=input("siapa nama anda:")
            file = open('C:/wiyan/sesi_2/sesi_6_tebak_kata.txt', 'w')
            file.close()
            with open('C:/wiyan/sesi_2/sesi_6_tebak_kata.txt' , 'w') as f:
                f.write(topscorename)
        else:
            print("anda belum mencetak top score")
            break
    else:
        cobatebak=""
        print("masih salah")
else:
    print("file empty")
            
        
        
        

      
    
    