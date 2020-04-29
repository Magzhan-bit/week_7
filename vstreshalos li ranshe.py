b = list(map(int, input().split()))
d = {}
for a in b:
    if a in d:
        print("YES")
    else:
        d[a] = 1
        print("NO")
