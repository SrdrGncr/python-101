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

print(""" 
        \rPYTHON NOTLARIM :\n1-VERİ TİPLERİ\t
        \r2-DEĞİŞKENLER\n\r3-PRİNT FONKSİYONU\t\r4-STRİNG VERİ TİPLERİ\n""")# Print fonksiyonu çıktı vermek için kullanılır
                                                                                                           # Operatorler ile string veri tiplerinde işlemler yapılabilir
                                                                                                           # Özel anlam taşıyan string karakterlerikullanmak için kaçış dizeleri kullanılır.     

                                                                                                            # \ = tınrak işarteleri kullanımında kullanılır
                                                                                                            # \n = satır başı
                                                                                                            # \t = sağ tarafa doğru 4 satır boşuk bırakır
                                                                                                            # \r = Satır başı
                                                                                                            # \v = düşey sekme
                                                                                                            # \b = imleç kaydırma
print(""" işlem sonuçları """,topla,cikar,carp,bol,kalan,kalan2,"\a")

