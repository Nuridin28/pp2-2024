import re
with open('row.txt', 'r') as file:
    data = file.read()

x = re.findall('[A-Z]{1}[a-z]+', data)
print(x)
