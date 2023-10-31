print("""
**************

Kullanıcıdan bir tam sayı istensin.
Tam sayı aşağıdaki koşullara sahip ise 'Garip' ; değilse 'Garip Değil' yazsın.
Tek sayı ise; 'Garip'
Çift sayı ise ve 2-5 aralığında ise (2 ve 5 dahil); 'Garip Değil'
Çift sayı ise ve 6-20 aralığında ise (6 ve 20 dahil); 'Garip'
Çift sayı ise ve 20'den büyük ise (20 dahil değil); 'Garip Değil'

**************
""")


sayi = int(input("Lütfen bir tam sayı giriniz: "))

if sayi % 2 != 0 :
    print("""
        Bu sayı tek sayıdır.
        Garip""")
else:
    print("Bu sayı çift sayıdır.")
    if sayi>=2 and sayi<=5:
        print("Garip Değil")
    elif sayi>=6 and sayi<=20:
        print("Garip")
    elif sayi>20:
        print("Garip Değil")



