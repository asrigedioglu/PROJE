#Bir sayının tam bölenlerini hesaplayın

def factoring(number):
    factor = []
    for e in range(1,number + 1):
        if number % e == 0:
            factor.append(e)
    return factor
        

while True:
    input_value = input("Lütfen değer giriniz: ")
    
    if input_value == "q":
        print("Program sonlandı.")
        break
        
    else:
        number = int(input_value)
        print(f" {number} sayısının çarpanları: {factoring(number)}")
    
