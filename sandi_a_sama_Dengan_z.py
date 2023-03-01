sandi1='abcdefghijklmnopqrstuvwxyz'
panjang=len(sandi1)
awal=-1
sandi2=''
for i in range(panjang-1,awal,-1):
    sandi2=sandi2+sandi1[i]
    print(sandi1[i])
print(sandi2)
hasilenkripsi=""
inputan=input('ketik kata yang akan dienkripsi (a=z) dengan huruf kecil: ')
panjanginputan=len(inputan)
awal=0
for i in range(0,panjanginputan):
    awal=0
    for j in range(awal,panjang-1):
       if inputan[i]!=" ":
         if inputan[i]==sandi1[j]:
             hasilenkripsi=hasilenkripsi+sandi2[j]
         else:
            continue
       else:
           hasilenkripsi=hasilenkripsi+" "
print(hasilenkripsi)