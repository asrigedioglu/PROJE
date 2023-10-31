import datetime

users = {"asrı":"ocak","nezih":"eylül","emel":"temmuz","hayat":"ekim","gülden":"aralık","poyraz":"ekim"}

limit = 4
count = 0

while count < limit :
    
    user_id = input("Yaş hesaplama uygulamasına Hoşgediniz! Lütfen kullanıcı adınızı giriniz: ")
    user_password = input("Parola: ")
    
    if user_id in users.keys() and user_password == users[user_id]:
        print("Giriş başarılı")
                
        birth_date = int(input("Doğum tarihinizi giriniz: "))
        current_date = datetime.datetime.now()
        current_year = current_date.year
        age = current_year - birth_date
        print(f'Şuanda {age} yaşındasınız.')
                
        break
                
                
    else:
        count += 1
        
        if user_id in users.keys(): 
            print("Parola yanlış. Lütfen tekrar giriniz.")
        else:
            print("Kullanıcı adı hatalı")
        
        if count >= 3:
                print("Maksimum 3 kere hatalı kullanıcı adı girebilirsiz. ")
                break
            

        
