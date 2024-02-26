import re
with open('row.txt', 'r') as file:
    data = file.read()

x = re.findall('[a-z]+\_+', data)
print(x)
