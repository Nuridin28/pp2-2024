import re

with open('row.txt', 'r') as file:
    data = file.read()

x = re.findall('ab{2,3}', data)
print(x)