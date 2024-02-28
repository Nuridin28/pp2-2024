x = open("created_file.txt", "w")

st = list(input().split())
c = 1
for i in st:
    x.write(str(c) + " : ")
    i += '\n'
    x.write(i)
    c+= 1