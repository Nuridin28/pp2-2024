def rev(s):
    r = s[::-1]
    for i in r:
        print(i, ' ', end = '')

str = list(input().split())
rev(str)