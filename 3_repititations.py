a = list(input())
cnt = 1
mx = 1
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        cnt += 1
    elif a[i] != a[i+1]:
        cnt = 1
    mx = max(mx, cnt)
print(mx)