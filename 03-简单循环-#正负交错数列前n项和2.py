n = int(input())
a = 1
b = -1
c,d = 1,1
for i in range(1,n):
    c,d =c,c+d
    a = a+b*i/d
    b = -b
print("{:.6f}".format(a))
