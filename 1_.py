n = int(input())
ls = list()
while(True):
    #print(n)
    ls.append(n)
    if n==1:
        break
    if n%2 ==0:
        n = n//2
    elif n%2 ==1:
        n = n*3+1
print(*ls)