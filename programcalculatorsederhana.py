# Start Code Here
import time
print("Program Calculator Sederhana untuk 2 bilangan")
print("pilih proses")
print("1.Penjumlahan")
print("2.pengurangan")
print("3.Perkalian")
print("4.pembagian")
pilihan = int(input("pilih Proses diatas dengan input nomornya saja:"))
if pilihan == 1:
  bil1 = int(input("masukan bilangan satu 1:"))
  bil2 = int(input("masukan bilangan satu 2:"))
  hasil = bil1 + bil2
  print(hasil)
if pilihan == 2:
  bil1 = int(input("masukan bilangan satu 1:"))
  bil2 = int(input("masukan bilangan satu 2:"))
  hasil = bil1 - bil2
  print(hasil)
if pilihan == 3:
  bil1 = int(input("masukan bilangan satu 1:"))
  bil2 = int(input("masukan bilangan satu 2:"))
  hasil = bil1 * bil2
  print(hasil)
if pilihan == 4:
  bil1 = int(input("masukan bilangan satu 1:"))
  bil2 = int(input("masukan bilangan satu 2:"))
  hasil = bil1 / bil2
  print(hasil)
