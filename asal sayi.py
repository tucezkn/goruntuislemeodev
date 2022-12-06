a=int(input("bir sayı giriniz : "))
if a > 1:
    for i in range(2,a):
        if(a%i)==0:
            print(a, "Asal sayı değildir.")
            break
        else:
            print(a, "Asal sayıdır.")    
else:
    print(a, "asal sayı değildir.")