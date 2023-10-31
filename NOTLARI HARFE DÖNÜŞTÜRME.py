print("""
Bu program öğrenci notunun harfdilimine yuvarlanmasıdır.
      """)

str_puan  = input("Lütfen aldığınız puanı giriniz: ")

if "," in str_puan :
    print(f'Virgül kullanımı {str_puan.find(",")}. index"te yer alır.')
    str_puan = str_puan.replace(",",".")
    puan = float(str_puan)
    print(f'Girdiğiniz puan: {puan}')
    
else:
    print("Girdiniz sorunsuz ilerliyor.")
              
if 0<=puan and puan<=100:
    print("Veri doğrulaması başarılı...")

    if puan > 80:
            print("Öğrenci harf notu : A")
    elif 60 < puan:
            print("Öğrenci harf notu : B")
    elif 40 < puan:
            print("Öğrenci harf notu : C")
    elif 20 < puan:
            print("Öğrenci harf notu : D")
    elif 0 < puan:
            print("Öğrenci harf notu : E")

else:
    print("Hatalı giriş yaptınız")

## Alternatif Çözüm
    
while True:
    puan  = float(input("Lütfen aldığınız puanı giriniz: "))

    if puan > 100:
        print("uygulamadan çıkıyorsunuz")
        break
        
    else:        
        if 0<=puan and puan<=100:
            print("Veri doğrulaması başarılı...")

            if puan > 80:
                    print("Öğrenci harf notu : A")
            elif 60 < puan:
                    print("Öğrenci harf notu : B")
            elif 40 < puan:
                    print("Öğrenci harf notu : C")
            elif 20 < puan:
                    print("Öğrenci harf notu : D")
            elif 0 < puan:
                    print("Öğrenci harf notu : E")

        
