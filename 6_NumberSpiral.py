for i in range(int(input())):
    x,y = map(int, input().split())
    M = max(x,y)
    print((x-y)*(-1)**M+M*M-M+1)