sayi1 = int(input("Sayı 1: "))
sayi2 = int(input("Sayı 2: "))
 
print(sayi1,"ile",sayi2,"arasındaki çift sayılar:")
 
for sayi in range(sayi1,sayi2):
       if(sayi%2)==0:
        print(sayi)
       
