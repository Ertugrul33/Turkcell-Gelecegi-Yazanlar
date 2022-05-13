
import HesapModulu #1. Modül Kullanma Tekniği (Direkt kendisini çağırma)

HesapModulu.yeni_maas(1000)

HesapModulu.yeni_maas(2000)

import HesapModulu as hm #2. Modül Kullanma Tekniği (Özel isimle kullanma)

hm.yeni_maas(1000)

from HesapModulu import yeni_maas #3. Modül Kullanma Tekniği (Modülün içerisindeki bir fonksiyonu kullanma)

yeni_maas(4000)

import HesapModulu as hm

hm.maaslar #Bir fonksiyonu değil de herhangi bir nesneyi (değişkeni) de çağırabiliriz.
