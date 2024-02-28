st = input()
u,l =0, 0
for ch in st:
    if ch.isupper():
        u+=1
    if ch.islower():
        l+=1

print("count of lower case ", l)
print("count of upper case ", u)