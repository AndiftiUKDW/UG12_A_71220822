x = str(input("masukan nama : "))
count = len(x)
for i in range(count):
    print(x[0:i+1])
count = count - 2
while count!=-1:
    print(x[0:count+1])
    count = count -1