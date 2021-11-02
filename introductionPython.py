# VERİ TİPLERi
# DEĞİŞKENLER
# PRİNT FONKSİYONU
# STRİNG VERİ TİPLERİ:

sayi1 = 50                        # Değişlenler bellekte verilen veri tipi kadar yer tutar
sayi2 = 10.50                     # Pythonda integer ve float tam sayı veri tipleri vardır.

karakter = """ PYTHON DERS 1 """  # String veri tipleri tırnak içerisine alınır.
                                  # Tırnak içerisine alınan her şey string veri tipi olur
                                  # " A " , """ A """, 'A ' şeklinde tırnaklar kullanılabilir.

topla = sayi1 + sayi2             # Sayılarla işlem yapmak için operatörler kullanılır. 
cikar = sayi1 - sayi2             # Operatörlerle string veri tipleri ilede işlem yapmak mümkündür
carp  = sayi1 * sayi2
bol   = sayi1 / sayi2
kalan = sayi1 % sayi2
kalan2= sayi1 // sayi2

print(5*"#"+karakter+5*"#")       # Print fonksiyonu çıktı vermek için kullanılır
                                  # Operatorler ile string veri tiplerinde işlemler yapılabilir

print(""" işlem sonuçları """,topla,cikar,carp,bol,kalan,kalan2)

