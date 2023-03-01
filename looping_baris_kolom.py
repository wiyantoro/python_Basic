import time
import random
minbaris=1
maxbaris=5
stringbintang=""
#looping baris
while True:
    inputan=random.randint(1,11)
    print("nila random:",inputan)
    minbaris=1
    while(minbaris<=inputan):
   #looping baris
       minkolom=1
       maxkolom=minbaris
       while(minkolom<=maxkolom):
           if minkolom==1:
               stringbintang=" * "
           else:
               stringbintang=stringbintang+" * "
           minkolom+=1
       print(stringbintang)
       time.sleep(1)
       minbaris+=1