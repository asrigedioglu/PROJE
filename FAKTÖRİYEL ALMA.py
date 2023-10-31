while True:
    deger = input("Lütfen numerik bir değer giriniz: ")

    if deger == "q":
        print("Döngüden çıkıyorsunuz")
        break

    elif deger.isdigit():
        
        result = 1
        for i in range(1,int(deger)+1):
            result *= i
        print(f"{deger} faktoriyeli: {result}")
        
    else:
        print("Hatalı giriş yaptınız.Lütfen numerik bir değer giriniz")
