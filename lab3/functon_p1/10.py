def uniq(l):
    ans = []
    l.sort()
    #1 1 2 2 3 3
    for i in range(len(l) - 1):
        if l[i] == l[i+1]:
            continue
        else:
            ans.append(l[i])

    ans.append(l[-1])
    print(ans)


x = list(input().split())
for i in range(len(x)):
    x[i] = int(x[i])

uniq(x)