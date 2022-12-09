awal = int(input("Masukan awal deret: "))
akhir = int(input("Masukan akhir deret: "))
for i in range(awal,akhir+1):
    if(i%2!=0):
        if(i%3==0 or i%6==0):
            continue
        else:
            print(i, end=" ")
