n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1,n):
    if a[i] <= a[i-1]:
        p = a[i-1] - a[i]
        ans = ans + p
        a[i] += p

print(ans)