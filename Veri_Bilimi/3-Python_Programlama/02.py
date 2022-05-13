# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:18:55 2020

@author: Samed
"""

##SINIF YONELIMLI PROGRAMLAMA

##Sinif Nedir ? Nasıl oluşturulur

class VeriBilimci():
    print("Bu bir sınıftır")
    
##Sinif Ozellikleri (Class attributes)

class VeriBilimcisi():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0 
    bildigi_diller = []
    
    
##Siniflarin özelliklerine erismek    
    
VeriBilimcisi.bolum
VeriBilimcisi.sql

##Siniflarin özelliklerini degistirme
VeriBilimcisi.sql = "Hayır"
VeriBilimcisi.sql

##Sinif Orneklendirmesi(instantiation)

ali = VeriBilimcisi

ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimcisi()
veli.sql

veli.bildigi_diller

##Ornek ozellikleri

class VeriBilimcisi():
    bildigi_diller = ["R","Python"]
    bolum = ''
    sql = ''
    deneyim_yili = 0 
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = []
        
ali = VeriBilimcisi()
ali.bildigi_diller        


veli = VeriBilimcisi()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller
veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimcisi.bildigi_diller

ali.bolum

VeriBilimcisi.bolum
ali.bolum = "istatistik"
VeriBilimcisi.bolum
veli.bolum
veli.bolum = "end_muh"
veli.bolum
ali.bolum
VeriBilimcisi.bolum


##Ornek Metodlari(fonksiyonlu)

#ornekler üzerinde çalışan fonksiyonlar yazmak 

class VeriBilimcisi():
    calisanlar = [] 
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
ali = VeriBilimcisi()        
ali.bildigi_diller
ali.bolum

veli = VeriBilimcisi()        
veli.bildigi_diller
veli.bolum

dir(VeriBilimcisi)

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller


##Miras Yapıları(inheritance)

class Employees():
     def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
        
        
class DataScience(Employees):  #her veri bilimcisinin ismi,soyismi vs olduğu için ordaki özellikleri miras olarak bu sınıftada parantez içerisine Employees(çalışanlar)  yazarak kullandık
     def __init__(self):
        self.Programming = ""
        
veribilimci1 = DataScience()
veribilimci1.        
        
class Marketing(Employees):
     def __init__(self):
        self.StoryTelling = ""  #ürünün anlatılma yeteneği


mar1 = Marketing()
mar1.

#yeni bir çalışan eklemek içinfonksiyonlu sınıfı aşağıdaki gibi de tanımlayabiiriz

class Employees_yeni():
     def __init__(self, FirstName,Soyadi,Address):
        self.FirstName = FirstName
        self.LastName = Soyadi
        self.Address = Address
        
# ali çalışanını aşağıdaki gibi ekleyebiliriz

ali = Employees_yeni("Samet","Karasu","Turkey") 
ali.FirstName
ali.LastName


##Python'da Fonksiyonel Programlama

#Fonksiyonlar dilin baştacidir
#(Birinci sinif nesnelerdir)
#Yan etkisiz fonksiyonlar. (stateless, girdi-çıktı)
#Vektorel operasyonlar

##Yan Etkisiz Fonksiyonlar(Pure Functions)

##Ornek1:Yan etki

#Burada aşağıdaki fonksiyonda A ya bağlı bir fonksiyondur. Bu sebeple bunlara yan etkiye sahip fonksiyon denir.

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6)
pure_sum(3, 4)

##Ornek2: Olumcul yan etkiler

#OOP(Nesne yönelimli programlama ile)
class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)
    
lc = LineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())


#Fonksiyonel Programlama(üsteki dosya işlemini fonksiyonel programlama ile yapıyoruz)
#FP

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
lines_count


##Isimsiz Fonskiyonlar (Anonymous Functions)

##isimli fonksiyon
def old_sum(a,b):
    return a + b 

old_sum(4,5)

#isimli ancak lambda ile oluşturulan bir fonksiyon
new_sum = lambda a,b : a+b
new_sum(4,5)

###

sirasiz_liste = [('b',3),('a', 8),('d', 12),('c', 1)]
sirasiz_liste

##isimsiz fonsiyon 

#Her bir tuple in içindeki 1. indexi büyükten küçüğe doğru sıralayan isimsiz bir fonksiyon yazalım:
sorted(sirasiz_liste, key = lambda x: x[1])


##Vertorel Operasyonlar (Vectorel Operations)
##OOP(NYP)

#dizideki elemanları çarpan bir program yazalım:
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0, len(a))

for i in range(0, len(a)):
    ab.append(a[i]*b[i])
    
ab    

#FP
#yukardaki işlemi FONKSİYONEL PROGRAMALAMA ile çok daha kısa şekilde yapalım:

import numpy as np 

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b

##map & filter & reduce

##map
#her dizeye 10 ekliyoruz
liste = [1,2,3,4,5]

for i in liste:
    print(i+10)
   
    
#aynısını isimsiz fonksiyon ile yapıyoruz 
list(map(lambda  x: x+10, liste))    

##filter

#ikiye bölündüğünde sıfır kalan değerlere ulaşmak istiyoruz.
liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0, liste))

##reduce #-----> tek sonuc verir(tek deger dondurur)

##indirgeme işlemi yapar

from functools import reduce

liste = [1,2,3,4]
reduce(lambda a,b: a + b, liste)


##Modul Olusturmak

#HesapModlulu nu kullanalım

import HesapModulu 

HesapModulu.yeni_maas(1000)

#simdi ise hesapmodulune daha kısa ad vererek kullanacagız

import HesapModulu as hm #HesapModulunun ismini hm yaptık
hm.yeni_maas(1000)

#fonksiyonun kendisini modulun icerisinden çağıralım

from HesapModlulu import yeni_maas
yeni_maas(4000)


#son olarak hesap modulundan maasları cağırdık.
import HesapModlulu as hm
hm.maaslar


##Hatalar / istisnalar (exceptions)

# bölünme hatasi
a = 10 
b= 0 

a/b

try:
    print(a/b)
except  ZeroDivisionError:
    print("Payda da sifir olmaz")
          
#tip hatasi

a = 10 
b = "2"

a/b          

try:
    print(a/b)
except  TypeError:
    print("sayi ve string bir birine bölünmez")
    
## THE END     


#SORULAR

liste = [1,2,3,4]
A = []

for i in liste:
    A.append(i**2)

print(A)


---------------------

def yap(x,y,z):
    try:
        print(x/y*z)
    except ZeroDivisionError:
        print("gecersiz islem")

yap(1,2,0)

------------------

list(map(lambda x: x*1, [2,7,4]))

--------------

liste = ["a",20,10,30,"b"]
list(filter(lambda x: type(x) == int, liste))

----------------

from functools import reduce
reduce(lambda a,b: a+b, ["a","4","a"])


---------------

A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A, B]

for i in AB:
    if type(i[0]) == str:
        print(list(map(lambda x: x + " hi", i)))
        
------------------

class BolumSorulari():
    fonksiyonlar = []
    OOP = []   

donguler = BolumSorulari()  

donguler = BolumSorulari("fonksiyonlar")  

----------------------

A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A,B]


for i in AB:
    if type(i[0]) == int:
        print(list(map(lambda x: x-3, i)))
        
-------------------------       

list(filter(lambda x: len(x) > 8, ["pazartesi","sali","carsamba","persembe","cuma"])) 

-------------------------

from functools import reduce
A = ["Veri","Bilimi","Okulu"]
reduce(lambda a,b: a+b, list(map(lambda x: x[0], A)))



##----> aşağıdaki her ikiside aynı sonu verir
print(list(map(lambda x: x, A))) 


A[0][0] 
A[1][0]
A[2][0]

---------
#öncelik ***
list(map(lambda x: x/10, filter(lambda x: x > 20, [10,20,30,40,50])))


--------------

from functools import reduce
reduce(lambda a,b: a/b, [8,4,2])

-------------------


list(map(lambda x: x.upper(), ["Ali","Veli","isik"]))

---------------------

import numpy as np
a = np.array([1,1,1])
b = np.array([2])

a+b

--------------------

A = [1,2,3,4,5]


if type(A) == ():
    print("islem gecersiz")
else:
    print(list(map(lambda x: x/1, A)))

type(A) == (): #----->> boş kümemi sorusunu sorar


