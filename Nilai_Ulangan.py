print("Nilai Ulangan Harian Murid")
inputan=int(input("ketikan nila murid range:(0-100):"))
if inputan>=0 and inputan<=49:
    print("nilai kamu adalah : E :semangat yaa belajarnya ")
else:
    if inputan>=50 and inputan<=59:
        print("nilai kamu adalah : D :ayokkk kamu pasti bisa ")
    else:
        if inputan>=60 and inputan<=69:
            print("nilai kamu adalah : C :sudah cukup baik ")
        else:
            if inputan>=70 and inputan<=79:
                print("nilai kamu adalah : B : kamu sudah baik ")
            else:
                if inputan>=80 and inputan<=100:
                    print("nilai kamu adalah : A :nilai kamu sangat baik ")
                else:
                    print("selamat kamu baik")
    