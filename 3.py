def polaUnik(panjang):
    for i in range(panjang):
        if i%2==0:
            print("*"*panjang)
        else:
            print("*"+"="*(panjang-2)+"*")
polaUnik(5)