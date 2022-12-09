batas = int(input("Masukan pembatas : "))
larang = int(input("Masukan Angka yang dilarang : "))

for i in range(batas):
    if(i==larang):
        continue
    else:
        print(i,end=" ")