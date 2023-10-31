import math
tek_indexler = [0,2,4,6,8]
cift_indexler = [1,3,5,7]
ilk_on = [0,1,2,3,4,5,6,7,8,9]

while True:

    tc_kimlik = input("Lütfen TC kimlik Numaranızı giriniz: ")

    if len(tc_kimlik) == 11:
        print("✓ TC KİMLİK NO 11 HANELİ")

        if int(tc_kimlik[0]) != 0:
            print("✓ TC KİMLİK NO İLK BASAMAK 0 DEĞİL")

            tek_toplam = 0 
            cift_toplam = 0
            ilk_on_toplam = 0

            for t in tek_indexler:
                tek_toplam += int(tc_kimlik[t])

            for c in cift_indexler:
                cift_toplam += int(tc_kimlik[c])

            for on in ilk_on:
                ilk_on_toplam += int(tc_kimlik[on])

            if ((tek_toplam*7) - cift_toplam) % 10 == int(tc_kimlik[9]):
                print(f'Tc kimlik no 10.hanesi: {tc_kimlik[9]}')
                print("✓ TC KİMLİK NO 10.BASAMAK DOĞRU")

                if ilk_on_toplam % 10 == int(tc_kimlik[10]):
                    print(f'Tc kimlik no 11. hanesi: {tc_kimlik[10]}')
                    print("✓ TC KİMLİK NO 11.BASAMAK DOĞRU")
                    print("""************************
                    ✓✓ TC KİMLİK NO DOĞRUDUR""")  
                    
                    break
                
                else:
                    print("!! TC KİMLİK NO 11.BASAMAK HATALIDIR !!")        
            else:
                print("!! TC KİMLİK NO'NUN 9.BASAMAKTAKİ SAYISI DOĞRU DEĞİL !! ")     
        else:
            print("!! İLK RAKAM 0 !!")
            
    else:
        print("!! TC KİMLİK NO 11 HANELİ DEĞİLDİR !! ")
        
    
