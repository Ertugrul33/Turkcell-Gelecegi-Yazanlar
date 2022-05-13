#PYTHON PROGRAMLAMA 101

#SAYILAR VE STRINGLERE GİRİŞ
9
9.2
9+9
9*9

print('HELLO AI ERA')
"HELLO AI ERA"

type(9)
type(9.2)
type("HELLO AI ERA")

#STRINGLERE YAKINDAN BAKALIM


''
""

123
type(123)
"123"
type("123")

"a" + "b"

"a" "b"
"a" " b"
"a" "-b"



"a" - "b"

"a"*3

"a "*3

"a"/3

#STRING METODLARI - len()

#METOD: Veri yapıları üzerine uygulanan çeşitli fonksiyonlardır.


gel_yaz = "gelecegi_yazanlar"
#del mvk -> Değişken silme metodu

a = 9
b = 10


a*b


len(gel_yaz)
len("gelecegi_yazanlar")

#STRING METODLARI - upper() & lower()


gel_yaz = "gelecegi_yazanlar"

gel_yaz.upper() #Bütün harfleri büyük yazar.
gel_yaz.lower() #Bütün harfleri küçük yazar.


gel_yaz.islower()

B = gel_yaz.upper()

B.islower()
B.isupper()


#Benim Denemem - capitalize()
C = gel_yaz.capitalize()
C.isupper()
C.islower()
#İki ifadede de "False" sonucunu döndürüyor. Çünkü kelime ne büyük ne de küçük.



#STRING METODLARI - replace()


gel_yaz = "gelecegi_yazanlar"

gel_yaz.replace("e", "a") #e'leri a ile değiştir.

gel_yaz

#Herhangi bir atama işlemi olmadığından "gel_yaz" değişkeninde bir değişiklik olmadı.(OOP'nin konusu)

gel_yaz.replace("a", "i")


#STRING METODLARI - strip()

#İstediğimiz karakteri sağdan ve soldan kırpma işlemi yapar.

gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip() #Kendisi boşlukları kırptı. Bu fonksiyonu yazanlar daha önce o şekilde tanımlamış.



gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip("*")


gel_yaz = "lgelecegi_yazanlarl"
gel_yaz.strip("l")

#METODLARA GENEL BAKIŞ


gel_yaz = "gelecegi_yazanlar"


dir(gel_yaz) #Değişkenin tipine göre uygulanabilecek metodları gösterir.

gel_yaz.capitalize()
gel_yaz.title() #Her bir kelimenin ilk harfini büyütür.


#SUBSTRINGLER 

#Elimizdeki stringlerin alt stringine erişme işlemine denir. (Slicing)
#Not: Bu sadece string ifadeler için geçerli değil, veri yapıları için de geçerlidir.

gel_yaz = "gelecegi_yazanlar"

gel_yaz[0]
gel_yaz[1]

gel_yaz[20]

gel_yaz[0:3] #Slicing - 0. index dahil, 3. index dahil değil.

gel_yaz[3:7]


#DEĞİŞKENLER

a = 9

b = "ali_uzaya_git"

c = a*2

a/c
a*c
a*5

type(100)
type(100.2)
type(1+2j)

a = 100.2


#TYPE_DÖNÜŞÜMLERİ

birinci_sayi = input()

toplama_bir = input()
toplama_iki = input()

type(toplama_bir)

toplama_bir + toplama_iki #Giriş işlemleri string aldığı için toplamadı.

int(toplama_bir) + int(toplama_iki)

11.0

int(11.0)

12

float(12)

str(12)

type(str(12))


#print()

print("HELLO AI ERA")

print("gelecegi","yazanlar", sep = "_") #sep: İki kelimeyi belirtilen ifade ile ayırma.

#Fonksiyonların genel amaçlarını "biçimlendirmek" için kullanılan alt görev belirticilere argüman denir.
#Burada "sep" bir argümandir.

#Örneğe göre "print" fonksiyonu bir yazdırma fonksiyonudur. Biz bu yazdırma amacını biçimlendirmek için
#kullandığımız "sep" bizim argümanımız oluyor.

#Yani fonksiyonun ön tanimli şekli ile değil, benim ifade ettiğim şekli ile yaz demek.

#Kısacası bir fonksiyonun alabileceği tüm işlevler argüman olarak tanımlanır.**


#PYTHON PROGRAMLAMA 201

#VERİ YAPILARI

#Listeler

# -Değiştirilebilirdir.
# -Farklı tipte veriler tutabilir(kapsayıcıdır).
# -Sıralıdır.

#[] veya list() ile kullanılır.

notlar = [90,80,70,50]

#list bir üst tiptir. (alt tipler int, string vs)

type(notlar)

liste = ["a",19.3,90]

liste_genis = ["a",19.3,90,notlar]

len(liste_genis) #Uzunluğu 4 olarak döndürür.

liste_genis[0]
liste_genis[1]
liste_genis[3]

type(liste_genis[0]) #liste_genis teki 0. elemanının tipini gösterir.


tum_liste = [liste, liste_genis]
#del tum_liste #del komutunu kullanmak istiyorsak başına "#" işareti konulması önerilir.(Bazı hataları almamak için)


#Listeler - ELeman İşlemleri


liste = [10,20,30,40,50]

liste[0]
liste[1]


liste[6]


liste[0:2]

liste[:2]

liste[2:]

yeni_liste = ["a",10,[20,30,40,50]]

yeni_liste

yeni_liste[3]
yeni_liste[2]

yeni_liste[0:2]

#Listenin içerisindeki bir listenin elemanına erişmek istiyorsak
yeni_liste[2][1]
#kod satırı kullanılır. (yeni_liste nin içerisindeki liste 2. indexte ve onun içindeki 1. indexe erişmek istedim.)

#Listeler - Eleman Değiştirme

liste = ["ali","veli","berkcan","ayşe"]
liste

liste[1] = "velinin_babası" 
#Veli'yi Veli'nin babası olarak değiştirdi. Çünkü bilindiği üzere liste işlemleri atama yöntem ile değiştirilebilir.

liste


liste[1] = "veli"
liste[0:3] = "alinin_babasi","velinin_babasi","berkcanın_babası"

liste

liste = ["ali","veli","berkcan","ayşe"]
liste

liste + ["kemal"] #Sadece Kemal'i görüntüleme işlemi yaptık. Listeye ekleme işlemi yapmak için atama işlemi yapılmalıdır.
liste

liste = liste + ["kemal"] #Listeye eklendi.
liste

#del liste[2] -> 2. indexteki elemanı sil.
liste


#Listeler - Liste Metodları

liste = ["ali","veli","ışık"]

dir(liste)

liste

#append & remove()

liste.append("berkcan")
#Listeye eleman ekleme fonksiyonu. Fakat bu ekleme durumu kalıcı olarak oldu.**

#1. Not: String ile alakalı fonksiyonlar geçici atama yaparken, liste ile alakalı fonksiyonlar ve atama işlemi
#kalıcı olarak atama işlemi yapar.**

#2. Not: Bazı metodlar değişkenler üzerinde kalıcı değişiklikler yapabilir.**
liste

liste.remove("berkcan")

liste


#insert()


liste = ["ali","veli","ışık"]

liste

liste.insert(0, "ayşe") #Listenin 0. indexine "ayşe"yi ekler. Fakat "ali"yi kaldırmaz. "ali"yi yan indexe koyar.
liste

liste = ["ali","veli","ışık"]

liste[0] = "ayşe" #Listenin 0. indexine -"ali"yi sil- "ayşe"yi ata.

liste.insert(2, "mehmet")
liste

liste.insert(5, "berk")
liste

len(liste)

liste.insert(len(liste),"beren") #Listenin uzunluğunu çağırarak listenin sonuna eleman eklendi. Zekice :)
liste

#pop

#İstenilen bir indexteki elemanı silmek için kullanılır.
liste.pop(0)
liste

liste.pop(4)
liste

#count

liste = ["ali","veli","ışık","ali","veli"]
liste

liste.count("ali") #Listede kaç tane "ali" olduğunun sonucunu döndürür.
liste.count("veli")
liste.count("ışık")

#copy

liste_yedek = liste.copy() #Listenin kopyasını alır ve "liste_yedek"e aktarır.

#extend

liste.extend(["a","b",10]) #İki listeyi birleştirmek amacıyla kullanılır.
liste

#index

liste.index("ali") #"ali" nin kaçııncı indexte olduğunun bilgisini verir.

#reverse

liste.reverse() #Elemanı tersten yazdırma.
liste

#sort

liste = [10,5,40,90]
liste.sort() #Listenin elemanlarını sıralar. Fakat liste sayısal değerler içermeli.
liste

#clear

liste.clear() #Listenin tüm elemanlarını siler.
liste


#Veri Yapıları - Tuple

#Tuple Oluşturma

#Listeler ile hemen hemen benzerdir.

# -Farklı türde veri saklayabilir. (kapsayıcıdır)
# -Sıralıdır. (indexleme olarak)
# -"Değiştirilemez" olmasıdır. (listelerden en önemli farkı)**


t = ("ali","veli",1,2,3.2,[1,2,3,4]) # 1. yöntem
t = "ali","veli",1,2,3.2,[1,2,3,4] # 2. yöntem
#tuple() 3. yöntem

#Normal parantez ile, hiçbir operatör kullanmadan veya "tuple()" fonksiyonu ile tuple oluşturulabilir.

t = ("eleman")
type(t)
# String olarak döndürdü. Eğer bunun tuple olmasını istiyorsak sonuna virgül konulmalı.

t = ("eleman",)
type(t)

#Tuple Eleman İşlemleri

t = ("ali","veli",1,2,3.2,[1,2,3,4])
t

t[1]
t[0:3]

t[2] = 99 #Hata verecektir. Çünkü bilindiği üzere tuple yapısı atama işlemini desteklemez.


#Veri Yapıları - Dictionary (Sözlük)

#Sözlük Oluşturma

#Listelere benzerdir.

# -Farklı türde veri saklayabilir. (kapsayıcıdır)
# -Sırasızdır. (listelerden farklı olarak)**
# -Değiştirilebilirdir.

#Anahtar ifadeler(key) ve anahtar ifadeye karşılıklarının(value) bir arada tutulduğu bir veri yapısıdır. Referanslı bir veri yapısıdır.
#Listelerde olduğu gibi index işlemi yapılmaz.
#Türkçedeki sözlük ifadesine çok benzerdir.

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}

#Süslü parantez ile sözlük olulturulur.
sozluk

len(sozluk) #6 eleman değil, 3 elemanlıdır. (Key ifadeler sayılmalıdır.)

sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART": 30}

sozluk

sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE",20],
          "CART": ["SSE",30]}

sozluk

#Sözlük Eleman İşlemleri

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk[0] #İndexleme olmadığından dolayı hata verir. O yüzden anahtar ifadeyi yazmamız gerekiyor.

sozluk["REG"] #Küçük-büyük harfe duyarlıdır. "reg" ifadesinde hata verecektir.

sozluk["LOJ"]

#Sözlük içinde birden fazla değer
sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE",20],
          "CART": ["SSE",30]}

sozluk["REG"]

#Sözlük içinde sözlük
sozluk = {"REG" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30},
          
          "LOJ" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30},
          
          "CART": {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30}}

sozluk
sozluk["REG"]["SSE"] #Eğer iç içe sözlük varsa eleman çağırma işlemi bu şekilde yapılır.

#Sözlük - Eleman Ekleme & Değiştirme

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk["REG"] = "Çoklu Doğrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Ağları"
sozluk

l = [1]
l

sozluk[l] = "yeni bir şey"

#Hata verir. Çünkü sözlüklerdeki "key" ifadeleri ancak "sabit veri yapıları" ile oluşturulabilir.
#Yani sözlükteki "key" bir liste olamaz. Çünkü listeler değiştirilebilir bir veri yapısıdır.
#"Key"ler sabitliğinden endişe etmememiz gereken referans değerlerdir.
#Yani "key"ler değiştirilebir bir referans değeri olmamalıdır.
#Int ve stringler sabit bir veri yapısı olduğu için anahtar ifade olarak eklenebilir.

t = ("tuple",)

sozluk[t] = "yeni bir şey"
sozluk

#Tuple ifadeleri de anahtar ifade olarak eklenebilir. Çünkü tuple yapısı da değiştirilemez bir veri yapısıdır.
#Fakat sağ tarafa yani "value" kısmına istediğimiz bir ifadeyi koyabiliriz. Yani farklı veri tipleri ekleyebiliriz.,


#Veri Yapıları - Setler

# -Sırasızdır.**
# -Değerleri eşsizdir. Yani aynı değer birden fazla olamaz.**
# -Değiştirilebilirdir.
# -Farklı veri tipleri barındırabilir.

#Matematikteki kümelere benzer.

#Set Oluşturma

s = set()
s

l = [1,"a","ali",123]
s = set(l)
s

t = ("a","ali")

s = set(t)
s

ali = "lutfen_ata_bakma_uzaya_git"
type(ali)

s = set(ali)
s
#Aynı karakterleri almayıp sadece bir tanesini aldı. Yani "set" yapısı birden fazla karakteri tekilleştirir.

l = ["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]
l

s = set(l)
s
#Bir de "set" yapısı ekrana yazdırırken öncelikle sayıları yazdırır, sonra stringleri yazdırır ve harf sırasına göre sıralar.
#Indexleme olmadığı için böyle bir yazdırma işlemi yapar.

len(s)

l[0]

s[0] #Hata verir. Çünkü -bilindiği üzere- "set" yapısı indexlemeyi desteklemez.

#Eleman Ekleme & Çıkarma

l = ["gelecegi","yazanlar"]

s = set(l)
s

dir(s)

s.add("ile")
s

s.add("gelecege_git")
s

s.add("ali")
s

s.add("ile")
s
#Tekrar yazdırmayacaktır. Çünkü -bilindiği üzere- set yapılarında tekrar eden veriler içermez.

s.remove("ali") #Belirtilen elemanı sil.
s

s.remove("ali") #Hata verir. Çünkü içerisinde "ali" değeri yok.
s


#Eğer değer olmasa dahi hata almamak istiyorsak "discard" fonksiyonu kullanılır.
s.discard("ali")

#Setler - Klasik Küme İşlemleri


# =============================================================================
# #difference() -> iki kümenin farkını ya da "-" ifadesi
# #intersection() -> iki kümenin kesişimi ya da "&" ifadesi
# #union() -> iki kümenin birleşimi
# #symmetric_difference() -> ikisinde de olmayanları
# =============================================================================


#difference


set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) #set1'de olup set2'de olmayan değerleri gösterir.
set2.difference(set1)

set1.symmetric_difference(set2) #İkisinde de ortak olmayan değerleri yazdırır. {2, 5}

set1 - set2
set2 - set1
#difference işlemi bu şekilde de yapılabilir.


#intersection & union


set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)
set2.intersection(set1) #İki kümenin kesişimi

set1 & set2
set2 & set1
#kesişim işlemi bu şekilde de yapılabilir.

#Not: Bu işlemler yazdırılıyor fakat saklanmıyor.**

kesisim = set1 & set2

birlesim = set1.union(set2) #İki kümenin birleşimi
birlesim

set1.intersection_update(set2) #İki kümenin kesişimini alır ve set1'i günceller.
set1


#Setlerde Sorgu İşlemleri


set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])


#İki Kümenin Kesişiminin Boş Olup Olmadığının Sorgulanması


set1.isdisjoint(set2)


#Bir Kümenin Bütün Elemanlarının Başka Bir Küme İçerisinde Yer ALıp Almadığının Sorgulanması
#Yani Bir Küme Diğer Kümenin Alt Kümesi Midir?


set1.issubset(set2)


#Bir Kümenin Diğer Bir Kümeyi Kapsayıp Kapsamadığının Sorgulanması


set2.issuperset(set1)


# =============================================================================
# Özet olarak
# 
# Listeler "[]"            Tuple "()"              Sözlük "{}"             Setler "set()"
# Değiştirilebilir         Değiştirilemez          Değiştirilebilir        Değiştirilebilir
# Sıralı                   Sıralı                  Sırasız                 Sırasız - Eşsiz
# Kapsayıcı                Kapsayıcı               Kapsayıcı               Kapsayıcı
# =============================================================================


#PYTHON PROGRAMLAMA 301


#FONKSİYONLARA GİRİŞ VE FONKSİYON OKURYAZARLIĞI


print()
print

#Fonksiyon: Belirli görevleri yerine getirmek üzere genel amaçlar taşıyan görevciler(işleçler)dir.

?print 
#Fonksiyonun görevlerini görmek için kullanılır(fonksiyon okuryazarlığı). 
#Yani fonksiyona ilişkin gerekli dökümantasyona ulaşmaktır.

print("a","b", sep="_")

#Argüman: Fonksiyonların genel amaçlarını biçimlendirmek için kullanılar yapılardır.
#Yani fonksiyonun yapacağı iş için gereken yapıları oluşturmaktır.
#Bu argümanlar genelde virgül ile ayrılır.


len() #len fonksiyonu 1 tane argüman alır hatası verir.
len("a")


#Matematiksel İşlemler

4*4
4/4
5-1
6+3
3**2
3**3

#Fonksiyon Nasıl Yazılır?

4**2

def kare_al(x):
    print(x**2)

#Fonksiyon tanımlamak için "def" ifadesi kullanılır. Sonra fonksiyonun adı yazılır ve argümanlar eklenir.
#":" ibaresi konulur ve yapacağı işlemler yazılır.
#<fonksiyon_tanımlama_ibaresi --> def> <fonksiyonun adı>(<argümanlar>):

kare_al(3)
kare_al(5)

#Az önce ekrana yazdırmadı. Ekrana yazdırmak için fonksiyona "print" fonkyonunu kullanmamız gerekiyor.
#Eğer ekrana yazdırmak yerine çıkan bu değer üzerinden işlem yapmak istersek "return" ifadesini kullanmamız gerekiyor.**
#Yani aslında bi nevi sonucu saklamak için kullanılır.
#Bir diğer anlamı ise çıktı girdi olarak kullanmak için "return" ifadesi yazılır.


#Bilgi Notuyla Çıktı Üretmek


def kare_al(x):
    print(x**2)

kare_al(5)


def kare_al(x):
    print("Girilen Sayının Karesi: " + x**2)

kare_al(5)
#"String ifadeler yalnızca string ifadelerle birleştirilebilir" hatası verdi. Çünkü sağ taraf sayısal bir ifade.
#Bunu düzeltmek için:
    
def kare_al(x):
    print("Girilen Sayının Karesi: " + str(x**2))
    
kare_al(3)

#ile düzeltilebilir.

#Şimdi de karesi alınmak istenilen sayıyı ve karesi alındıktan sonraki sonucu görmek isteyelim:

def kare_al(x):
    print("Girilen Sayı: " + str(x) + "\nKaresi: " + str(x**2))
    
kare_al(3)


#İki Argümanlı Fonksiyon Tanımlamak


def kare_al(x):
    print(x**2)
    

def carpma_yap(x, y):
    print(x*y)
    
carpma_yap(2, 3)


#Ön Tanımlı Argümanlar


?print


def carpma_yap(x, y):
    print(x*y)
    
    
carpma_yap(3) #Bir argüman yok hatası verdi. "y" argümanına ön tanım vermek istersek:

def carpma_yap(x, y = 1):
    print(x*y)

carpma_yap(3)

#Kullanışlı olması adına ve hata almamak adına argümanlarımıza ön tanım vermemiz gerekiyor.
#Not: Ön tanıma 1 verdik diye de her zaman 1 ile çarpmayacaktır.

print("HELLO AI ERA")
#"print" fonksiyonunda başka argümanlar olmasına rağmen ön tanımları boş olduğu için yazdığımız metin hata vermeden çalışacaktır.
#Biz de argümanalarımızı bu şekilde kullanmalıyız.

#Argümanların Sıralaması


def carpma_yap(x, y = 1):
    print(x*y)

carpma_yap(2, 3)

carpma_yap(y = 2, x = 3)
#Eğer yazdığımız argümanların sırasını bilmez, unutur ya da karıştırır fakat argümanların isimlerini biliyorsak 
#"carpma_yap(y = 2, x = 3)" bu şekilde de kullanabiliriz.
#Yani sıralamadan bağımsız olarak da argümanların isimlerini yazarak bu işlemleri gerçekleştirebiliriz.


#Ne Zaman Fonksiyon Yazılır?


#Program içerisinde tekrar eden görevleri yerine getirmek ve 
#var olan işleri daha programatik bir şekilde gerçekleştirmek için kullanılır.

#Fonksiyonlara neden ihtiyaç olduğunu daha iyi anlamak için bir örnek yapalım:
    
#Bir belediyenin sokaklarındaki aydınlatma direklerini düşünelim. Bu direklerde bazı sensörler yer alsın. Bu sensörlerin,
#ısı, nem, şarj durumu gibi özellikleri olsun.

(40*25)/90 #(Not: Bu işlem örnek olsun diye verildi. Herhangi bir teknik anlamı yok.)

#gibi tek tek bu işlemleri yapmak yerine fonksiyon yazılabilir.

def direk_hesap(isi, nem, sarj):
    print((isi + nem)/sarj)

direk_hesap(25, 40, 70)


#Çıktıyı Girdi Olarak Kullanmak - return


def direk_hesap(isi, nem, sarj):
    print((isi + nem)/sarj)

cikti = direk_hesap(25, 40, 70)
cikti
print(cikti)
direk_hesap(25, 40, 70)*9
#return'ü bilmediğimizi varsayıp çıkan sonucu tekrar kullanmak için deneme-yanılma yaptık ve hepsinde hata verdi.
#Not: Fonksiyonumuza print fonksiyonu kullandık diye 
#"direk_hesap(25, 40, 70)*9" şeklinde yazarak çıkan sonucu tekrar kullanacağımız anlamına gelmez. İlla ki return olacak :)


def direk_hesap(isi, nem, sarj):
    return (isi + nem)/sarj


cikti = direk_hesap(25, 40, 70)
cikti
print(cikti)
direk_hesap(25, 40, 70)*9
#Fonksiyonumuzda return kullandığımız için yukarıda deneme-yanılma yoluyla yaptığımız kod satırlarının hepsi çalışmış oldu.
#Not: print yazmadan yalnız return yazarak da o fonksiyonu kullanabiliriz.
#direk_hesap(25, 40, 70) şeklinde de fonksiyon çalışır.


#DİKKAT

def direk_hesap(isi, nem, sarj):
    return 
    (isi + nem)/sarj

#Bu şekilde kullanmaktan kaçın!! Sonuç dönmeyecektir. Çünkü fonksiyona ne yapacağını söylemeden return yazdık.
#Bu yüzden alt taraftaki kodu dikkate almadı.


#Local ve Global Değişkenler


x = 10 #Global Değişken
y = 20 #Global Değişken

def carpma_yap(x, y):
    return x*y #Local Değişkenler(belli bir alanda olduğu için)

carpma_yap(2, 3)

#Not: Global değişkenler kalıcı iken, local değişkenler geçicidir.


#Local Etki Alanından Global Etki Alanını Değiştirmek


x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi.")

eleman_ekle("ali")

eleman_ekle("veli")

x
#Python, local etki alanında x'i bulamadığı için global etki alanına geçti ve tanımladığımız x listesine ekleme yaptı.
#Onda da bulamasaydı hata verecekti.

x = []
#del x

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi.")

eleman_ekle("ali")


#KARAR & KONTROL YAPILARI


#True - False Sorgulamaları

sinir = 5000

sinir == 4000 #Sınır değişkeni 4000 mi diye soruyor.

sinir == 5000

5 == 4    

5 == 5
#Yani "==" ifadesiyle True-False sorgulamaları yapıyoruz.


#if


sinir = 50000
gelir = 40000

gelir < sinir

if gelir < sinir: #Gelir sınırdan küçük mü sorusunu sordu. "True" olduğu için alttaki kodu çalıştırdı.
    print("Gelir sınırdan küçük")
    print(gelir*2)


sinir = 50000
gelir = 60000

gelir < sinir

if gelir < sinir:
    print("Gelir sınırdan küçük")

#Hiçbir şey dönmedi. Çünkü koşul sağlanmadı.

if gelir > sinir:
    print("Gelir sınırdan büyük")


#else

sinir = 50000
gelir = 35000


if gelir > sinir:
    print("Gelir sınırdan büyük")
else:
    print("Gelir sınırdan küçük")


#Diğer Örnek

sinir = 50000
gelir = 50000


if gelir == sinir:
    print("Gelir sınıra eşittir.")
else:
    print("Gelir sınıra eşit değildir.")

#elif

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir:
    print("Tebrikler! Hediye kazandınız.")
elif gelir1 < sinir:
    print("Uyarı")
else:
    print("Takibe devam.")


if gelir3 > sinir:
    print("Tebrikler! Hediye kazandınız.")
elif gelir3 < sinir:
    print("Uyarı")
else:
    print("Takibe devam.")


if gelir2 > sinir:
    print("Tebrikler! Hediye kazandınız.")
elif gelir2 < sinir:
    print("Uyarı")
else:
    print("Takibe devam.")


#Mini Uygulama

sinir = 50000
magaza_adi = input("Mağaza Adı: ")
gelir = int(input("Geliriniz: ")) #input ile istenen bilgiler string olduğu için onu inte çevirmemiz gerekiyor.

if gelir > sinir:
    print("Tebrikler " + magaza_adi + "!")
elif gelir < sinir:
    print("Uyarı! Geliriniz çok düşük: " + str(gelir))
else:
    print("Takibe devam.")
    
    
#DÖNGÜLER - for

#İteratif işlemler yapmak için for döngüleri kullanılır.

ogrenci = ["ali","veli","ışık","berk"]

ogrenci[0]
ogrenci[1]
ogrenci[2]
ogrenci[3]

for i in ogrenci:
    print(i)
    
#Python der ki: for yazdın tamam döngü yapacağım anladım peki nerede yapacağımı ve gezebileceğim-temsil edebileceğim
#bir geçici değişken belirt.**

#for - Devam

maaslar = [1000,2000,3000,4000,5000]

maaslar[0]
maaslar[1]
maaslar[2]
maaslar[3]
maaslar[4]

#i değişkeni biz bu erişim işlemini tek tek yapmak yerine her bir elemanı temsil edecek ve 
#gezebilecek(döngüyle) bir geçici değişkendir.

for maas in maaslar:
    print(maas)
    
    
#Döngü ve Fonksiyonların Birlikte Kullanımı


def kare_al(x):
    print(x**2)

kare_al(2)

maaslar = [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)


#Maaşlara %20 zam yapılacak. Gerekli kodları yazınız.

1000*20/100 + 1000

maaslar[0]*20/100 + maaslar[0]
maaslar[1]*20/100 + maaslar[1]
maaslar[2]*20/100 + maaslar[2]

#döngü yazılacak
#fonksiyon yazılacak

def yeni_maas(x):
    print(x*20/100 + x)
    
yeni_maas(1000)
yeni_maas(2000)
yeni_maas(3000)

for i in maaslar:
    yeni_maas(i)
    

#Mini Uygulama
#if, for ve Fonksiyonları Birlikte Kullanmak

#Maaşı 3000'den fazla olanlara %10, maaşı 3000'den az olanlara %20 zam yapılacak. Gerekli kodları yazınız.

maaslar = [1000,2000,3000,4000,5000]

def az_maasa_zam(x):
    print(x*20/100 + x)
    
def cok_maasa_zam(y):
    print(y*10/100 + y)
    
for i in maaslar:
    if i < 3000:
        az_maasa_zam(i)
    else:
        cok_maasa_zam(i)
        

#break & continue

maaslar = [8000,5000,2000,1000,3000,7000,1000]

dir(maaslar)
maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("Döngü kesildi.")
        break #Eğer 3000'e eşitse döngüyü bitir.
    print(i)


for i in maaslar:
    if i == 3000:
        continue #Eğer 3000'e eşitse onu atla ve göstermeden devam et.
    print(i)

#while

#Şart sağlandığı sürece demektir.

sayi = 1

while sayi < 10: #Sayı 10'dan küçük olduğu sürece
    sayi += 1 #Sayıyı 1 arttır.
    print(sayi) #Ekranda göster.


#PYTHON PROGRAMLAMA 401


#NESNE YÖNELİMLİ PROGRAMLAMA


#Not: Nesne yönelimli programlama bilmeden de Veri Bilimci olunabilir. Fakat development anlamında, kodları anlamak babında
#konuyu bilmekte fayda var. Yine de bilelim di mi? :)

#Daha önce yaptığımız gibi bu yapılar da işlerimizi daha pratik yapmamızı sağlar.

#Sınıf Nedir?

#Benzer özellikler, ortak amaçlar taşıyan, metod ve değişkenleri olan yapılardır.
#Yani aynı amaçlı fonksiyonları  bir arada tutmak ve erişmek için kullanılır.(bir yönü bu şekilde)
#string, int gibi kendimiz de bir sınıf oluşturabiliriz.
    
#Sınıf Özellikleri (Class Attributes)

#Örneğin Veri Bilimcilerin genel geçer özellikleri olur. Bölümü, SQL bilgisi, Python bilgisi, deneyimi vs.
#İşte bunları tutmamıza yarayan yapılar sınıflardır.

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []
    
#Sınıfların Özelliklerine Erişmek

VeriBilimci.bolum
VeriBilimci.sql

#Sınıfların Özelliklerini Değiştirmek

VeriBilimci.sql = "Hayır"
VeriBilimci.sql

#Sınıf Örneklendirmesi (Instantiation)

#Veri Bilimcilerin hepsi aynı olmayabilir. Yani sınıfımızda tanımladığımız özellikler değişecektir.
#Bazısı SQL bilirken bazısı bilmeyebilir. Dolayısıyla bizim Veri Bilimci oluşturmamız gerekiyor. Buna göre:
#Genel sınıf özelliklerini barındıran alt kümeler(alt birimler) oluşturma işlemine "sınıf örneklendirmesi" denir.

ali = VeriBilimci() #VeriBilimci() sınıfının özelliklerini taşıyan bir birim oluşturduk. Yani "sınıf örneklemesi" yaptık.

ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci()
veli.sql
veli.bildigi_diller
#Bunda da Python yazdı. Çünkü biz Ali'ye Python bilgisini ekledik ve bu tüm sınıfı etkiledi.
#Yani biz bir örnekleme yaptığında artık onda da Python bilgisi gelecek. Bunu düzeltmenin yolu var.

#Örnek Özellikleri

#Örneklerin her birisinin kendi içinde değişebilir özelliklerden oluştuğu bilgisini Python'a vermemiz gerekiyor. Bunun için:

class VeriBilimci():
    bildigi_diller = ["R","PYTHON"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''

#Yani bu her bir ayrı örneklendirme için özellik tutma işlemini sağlıyor.

ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller #Boş döndü, sorun çözüldü.
veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimci.bildigi_diller
#Özelliği yok hatası aldık. O yüzden VeriBilimci sınıfına özellik eklememiz gerekiyor. (1235. satıra eklendi.)
VeriBilimci.bildigi_diller

VeriBilimci.bolum
ali.bolum = "istatistik"
VeriBilimci.bolum #Boş döndü.
veli.bolum
veli.bolum = "end_muh"
veli.bolum
ali.bolum
VeriBilimci.bolum

#Sınıftaki "self" ifadesi, örneklemleri temsil eder. Örnekleyerek oluşturmuş olduğumuz örneklerin temsil edilmesini, onlara bir
#işlem yapılmasını sağlayan temsilcidir.
#self ifadesi yerine başka bir ifadenin yazılması tavsiye edilmez.

#bildigi_diller,sql,bolum ve deneyim_yili değişkenlerin sınıfın özellikleri iken def'in içindeki değişkenler örneklerin özellikleridir.
#Not: Sınıfın özellik isimleri ile örneklerin özellik isimlerinin aynı olması tavsiye edilmez.

#def kısma örnek özellikleri(nitelikleri) yazmak yerine bir fonksiyon yazmak da isteyebiliriz.

#Örnek Metodları

#Örnek: Bir çalışan bir dil öğrendiğinde ekleme yapan fonksiyonu yazınız.

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil): #self kullanmamızın sebebi örnekleri temsil etmek ve onlara işlem uygulamak için kullanıyorduk.
        self.bildigi_diller.append(yeni_dil)

#Biz artık VeriBilimcinin kendisiyle değil(üst çatının özellikleriyle değil) onun özellikleri ile ilgileniyor olacağız.
#Örneklerle yani.

ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle #Hata aldık.
VeriBilimci.dil_ekle(ahmet, "R")

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller

#Not: Sınıflar da bir nesnedir.

#Miras Yapıları (Inheritance)

#Yeni bir sınıf oluşturduğumuzda daha önce oluşturduğumuz sınıfın özelliklerini taşısın istiyorsak buna "miras yapısı" denir.

#Örneğin yazılmış olan köklü bir uygulamaya bir güncelleme yapmak istiyorsak, sınıfları tekrar tekrar oluşturmak yerine
#o sınıfları miras olarak kullanabiliriz. Böyle durumlarda işimize yarar.

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""
        
veribilimci1 = DataScience()
veribilimci1.Programming #Yalnız bu yapı geldi. "Employees" sınıfını diğer sınıflara miras yapmamız gerekiyor.
veribilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
mar1.

#Employees sınıfını ve bugüne kadarki oluşturduğumuz sınıfları fonksiyonel şeklinde değil de sabit değerlerle oluşturduk.
#Yani Employees sınıfını birisi çalıştırmak istediğinde eğer bu sınıfın içerisinde değişken değerler olmasını isterse ve bu
#şekilde kullanılmasını isterse programcı bu sınıfları fonksiyonel bir şekilde oluşturması gerekir. Bunun yolu:

class Employees_yeni():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address

ali = Employees_yeni() #Hata verir. Argümanlarını yazmamız gerekiyor.
ali = Employees_yeni("a","b","c")
ali.FirstName
ali.LastName
ali.Address

#Python'da Fonksiyonel Programlama

#Fonksiyonlar dilin baştacıdır. Daha esnek bir çalışma yapısı vardır.
#Birinci sınıf nesnelerdir.
#Yan etkisiz fonnksiyonlar (statenless, girdi-çıktı). Yani hiçbir dış faktörden etkilenmezler. Ancak girdi verildiğinde çıktı verir.
#Yüksek seviye fonksiyonlar
#Vektörel operasyonlar

#Bir programı NYP özellikleri ile de yazabiliriz; FP özellikleri ile de yazabiliriz.
#Tek bir cümleyle daha esnek ve bizi daha iyi anlayan bir programlama yaklaşımıdır.

#Yan Etkisiz Fonksiyonlar (Pure Functions)

#Ornek1: Bağımsızlık

A = 5

def impure_sum(b): #Saf olmayan
    return b + A

def pure_sum(a, b): #Saf
    return a + b


impure_sum(6)
A = 9
impure_sum(6)
#Sonuç değişti. Yani bu fonksiyon dışarıya bağlı bir fonksiyon. Bu da bizi endişelendiriyor.
pure_sum(3, 4)
#Dışarıdaki bir değişkeni değiştirsek bile bu fonksiyon her zaman 7 değerini döndürecektir. İşte avantajı budur.

#Örnek2: Ölümcül Yan Etkiler
#OOP

#Dosyayı açıp içindeki satırları sayan bir sınıf
class lineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
    
lc = lineCounter('deneme.txt')

print(lc.lines)
print(lc.count()) #Önce 0 değerini döndürürken, (Biz bir girdi verdik ama sonuç dönmedi.)

lc.read() #Bunu çalıştırdıktan sonra, (Bunu çalıştırmak lazım ki sonuç dönsün. Yani program buna bağımlı oldu.)

print(lc.lines)
print(lc.count()) #6 değerini döndürdü.
#Bu bazen iyi bir şey olmasına rağmen bazen de problem çıkaracak bir durumdur.
#Yani "lc.read" fonksiyonuna bağlı olarak sonuç değişti.

#FP

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

example_lines = read("deneme.txt")
lines_count = count(example_lines)
lines_count

#Bunda ise yalnızca ben bir girdi yazdığımda yani ben bunu çalıştırdığımda sonuç döndürecektir.
#Yani bu fonksiyonlar birbirinden bağımsızdır. Birbirini etkilemiyor.

#İsimsiz Fonksiyonlar (Anonymous Functions)

#İsimli Fonksiyon
def old_sum(a, b):
    return a + b

old_sum(4, 5)

#İsimli Ancak Lambda İle Oluşturulan Bir Fonksiyon
new_sum = lambda a,b: a + b
new_sum(4, 5)

sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste

#Amacımız bu listeyi sayılara göre sıralamak. Bunu isimsiz fonksiyon ile yapmak istiyoruz.

#İsimsiz Lambda İle Oluşturulan Fonksiyon
sorted(sirasiz_liste, key = lambda x: x[1]) 
#sorted: Argüman olarak fonksiyon olabilen bir yapı. Görevi sıralama yapmak. Yani "sorted" fonk. argüman alarak başka bir fonk. aldı.
#Veri Biliminde sık kullanılan yapılardır.

#Vektörel Operasyonlar (Vectorel Operations)

#OOP
a = [1,2,3,4] #Bunlara aynı zamanda tek boyut olduğundan dolayı vektör denir.
b = [2,3,4,5]

#Amacımız her bir indexe karşılık gelen değerleri çarpmak olsun (1*2, 2*3, ...)

ab = []

range(0, len(a)) 

for i in range(0, len(a)):
    ab.append(a[i]*b[i])
    
ab

#Normalde for'un içine bir liste yazardık fakat a ve b listesinde ortak 4 tane veri olduğundan dolayı
#"range(0, len(a))" kod satırı ile 4'e kadar gitmesini belirttik.

#Bu yaptığımız OOP özellikleri ile döngü yazarak iki tane vektörü çarpmaktı.
#Fakat söz konusu matematik, istatistik, veri bilimi, makine öğrenmesi gibi işlemler olduğunda asla bu tip döngülere girmiyoruz.

#FP

import numpy as np #Numpy isimli modülü np olarak çalışma ortamıma getir demek.
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b

#map & filter & reduce

#Oluşturduğumuz fonksiyonlara argüman olarak başka bir fonksiyon da ekleyebiliriz. (sorted gibi)
#İşte bu davranışlara izin veren fonksiyonlara first-class fonksiyonlar denir.
#Bu fonksiyonlar kendilerine iteratif nesneleri ve fonksiyonları argüman olarak alarak işlemlerimizi oldukça kolay hale getirir.
liste = [1,2,3,4,5]

for i in liste:
    print(i+10)

#Şimdi bunu map yapısını kullanarak lambda mimarisi ile birlikte bir fonk. tanımlama ve bu şekilde vektör özelindeki işlemleri
#farklı bir şekilde ele alalım.

list(map(lambda x: x+10, liste))

#map fonk. yazılan bir vektörün içerisinde belirli bir fonksiyonu çalıştırma imkan verir. (isimsiz fonksiyonu)

#filter

#Bu da benzer şekilde iteratif bir nesne alarak çalışır. Burada filter fonksiyonu iteratif bir nesne alır, bu nesne üzerinden
#başka bir iteratif nesne oluşturulur ve iteratif nesne içinde aradığı şartın sağlandığı tüm elemanlar filtrelenir.

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0, liste))

#liste içerisinde yalnızca 2'ye bölümünden kalan 0'ları al.

#reduce

#map ve filter'a benzerdir fakat indirgeme işlemi yapar.
#Mesela filter fonk. 2'ye bölümünden kalan 0'ları getirdi. Başka bir işlem yapmadı.

from functools import reduce

liste = [1,2,3,4]
reduce(lambda a,b: a + b, liste)
#Tek bir değer döndü. (1+2+3+4)

#Modül Oluşturmak

#Kütüphane veya paket de denir.
#Modüller, belirli amaçları yerine getirmek için bir arada bulunan fonksiyonlar topluluğudur.

#HesapModulu.py
def yeni_maas(x):
    print(x*20/100 + x)
    
maaslar = [1000,2000,3000,5000]

#test

import HesapModulu #1. Modül Kullanma Tekniği (Direkt kendisini çağırma)

HesapModulu.yeni_maas(1000)

HesapModulu.yeni_maas(2000)

import HesapModulu as hm #2. Modül Kullanma Tekniği (Özel isimle kullanma)

hm.yeni_maas(1000)

from HesapModulu import yeni_maas #3. Modül Kullanma Tekniği (Modülün içerisindeki bir fonksiyonu kullanma)

yeni_maas(4000)

import HesapModulu as hm

hm.maaslar #Bir fonksiyonu değil de herhangi bir nesneyi (değişkeni) de çağırabiliriz.

#Hatalar / İstisnalar (Exceptions)

#Hatalar 3'e ayrılır:
#1- Programcının hataları
#2- Program hataları
#3- İstisna(exception) hataları

#1- Programcının hataları, syntax hatalardır. Kolayca görülüp düzeltilebilen hatalardır. Program çalışmaz.
#2- Program hataları, buglardır ve çözülmesi zor hatalardır. Program çalışır fakat istediğimiz sonuçları vermez.
#3- İstisnalar, programda bildiğimiz bazı hatalar ve bu hatalar gözlendiğinde programı durdurma, devam et demenin yoludur.

#ZeroDivisionError Hatası
a = 10
b = 0

a/b
#Programcının gördüğü hatayı kullanıcının almaması için kullanıcının anlayacağı bir uyarı ekranı yazmamız gerekiyor.

try:
    print(a/b)
except ZeroDivisionError:
    print("Paydada sıfır olamaz.")
    
#Biz bunu yazmakla programa demiş olduk ki:
#try'ın altına yazdıklarımı dene (bunun önceki satırlara bağımlılığı var), eğer çalışmazsa(eğer hatalı bir işlem olursa),
#bu şekilde çalışmayı sürdür ve programımı bozma.
#except kısmından sonra o hatayı yazdık yani o hatayı görmezden gel dedik. 
#Sonunda da bir bilgi notu yazdık ki orada bir problem olduğunu görelim(yazmayabilirdik).

#TypeError Hatası

a = 10
b = "2"

a/b

try:
    print(a/b)
except TypeError:
    print("Sayı ve metin hatası.")
    

a = 10
b = 2

a/b

try:
    print(a/b)
except TypeError:
    print("Sayı ve metin hatası.")
    
#Hata olmasa bile her ihtimale karşı da bu yapıları yazabiliriz.
#Hata olması ihtimalleri olan durumlarda da bu yapıları kullanabiliriz.

#Eğitmenden önemli bir not: Karşılaşacağımız bir hatada mutlaka Google'lama yapmamız gerekiyor. Kendimiz çözmemiz gerekiyor.
#Hatayı direkt kopyala ve Google Arama'ya yapıştır. Direkt cevabı çıkaracaktır.

#SORULAR

from functools import reduce
a = [1,2,3,4]
reduce(lambda a,b: a*b, a)

------------------------

def yap(x,y,z):
    try:
        print(x/y*z)
    except ZeroDivisionError:
        print("gecersiz islem")

yap(1,2,0)

-----------------------

A = [[1,2],[3,4],[5,6]]
list(map(lambda x: x[0]*3, A))

------------------

A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A, B]

for i in AB:
    if type(i[0]) == str:
        print(list(map(lambda x: x + " hi", i))) 
        
        
---------------

A = []
for i in ["ali","veli","isik"]:
    A.append(i.replace("i","a"))
print(A)

------------------

a = [1,2,3]
list(map(lambda x: x*2, a))

--------------

liste = ["a",20,10,30,"b"]
list(filter(lambda x: type(x) == int, liste))

--------------------

A = [1,2,3,4,5]

if type(A) == (): #type(A) boş küme mi demek.
    print("islem gecersiz")
else:
    print(list(map(lambda x: x/1, A)))

----------------------------------

from functools import reduce
reduce(lambda a,b: a+b, ["a","4","a"])

----------------------------

liste = [1,2,3,4]
A = []

for i in liste:
    A.append(i**2)

print(A)
 
	
list(map(lambda x: x**2, liste))

---------------------------

fun = lambda x: x**2
fun(3)





























