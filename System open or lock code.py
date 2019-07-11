kullaniciadi =(input("Kullanıcı isminizi giriniz:"))
if kullaniciadi == "mertcan26":
    print("Doğru şimdi şifrenizi giriniz.")
    i=0
    for i in range(i<=3):
        sifre = input()
        if sifre == "123":
            print("Şifre Doğru Hoşgeldiniz")
            break
        else:
            print("Şifre yanlış")
            i=i+1
            if i == 3:
                print("SİSTEM KİLİTLENMİŞTİR!")                
else:
    print("Yanlış kullanıcı adı")
