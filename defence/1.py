num = int(input())

a = (i for i in range(0, num+1) if i%3 == 0)

for x in a:
    print(x)
