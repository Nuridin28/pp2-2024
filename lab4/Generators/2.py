n = int(input())
a = (i for i in range(n+1) if i%2 == 0)

for i in a:
    print(i, end = ', ')

