def histogram(arr):
    for i in arr:
        for j in range(i):
            print('*', end = '')
        print(' ')

x = list(input().split())
for i in range(len(x)):
    x[i] = int(x[i])

histogram(x)