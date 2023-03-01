string1="adam"
string2=" "
pangjang=len(string1)
for i in range(0,pangjang):
    if i==2:
        string2=string2+'1234'+string1[i]
    else:
        string2=string2+string1[i]
print(string2)
#replace
string2=string2.replace("123", " ")
#remove/menghapus kata
string2=string2.removeprefix("a")
print(string2)