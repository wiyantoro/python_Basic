#login user
str1='wiyan'
str2=''
count=0
print("login")
username=input("Input your Username:")
username=username.lower()
password=input("Input your Password:")
password=password.lower()

with open('C:/wiyan/sesi_2/sesi_6_user_name.txt','r') as fileuser:
    
    for cek in fileuser:
     if str1 in cek:
        count+=1
        str3=cek.rstrip("/n")
        passwd=str3.split(",")
        if str2==passwd[1]:
            count+=1
if(count==2):
    print("Selamat Datang")
else:
    print("Anda Salah")
