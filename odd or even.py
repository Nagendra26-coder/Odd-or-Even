def lop(a,b):
    while a < b:
        print(a)
        a = a + 2

a=int(input("enter any number:"))
b=int(input("enter any number:"))

if a%2==0:
        x = int(input("1.even or 2.odd number\n"))
        if x==1:
            lop(a,b)
        if x==2:
            a=a+1
            lop(a,b)

else:
        x = int(input("1.even or 2.odd number"))
        if x == 2:
            lop(a,b)
        if x == 1:
            a = a + 1
            lop(a,b)
