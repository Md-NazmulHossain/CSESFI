n = int(input())
od=[]
ev = []
ls = []
ans = 1
n4 = [2,4,1,3]
if n==2 or n==3:
    print("NO SOLUTION")
if n ==4:
    print(*n4)
if n>4 or n==1:
    while n>0:

        if n%2==0:
            ev.append(n)
        if n%2==1:
            od.append(n)
        n -= 1
    ls = ev + od
    print(*ls)

