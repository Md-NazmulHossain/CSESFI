n = int(input())
ls = list(map(int, input().split()))
print(((n*(n+1))//2)-sum(ls))
