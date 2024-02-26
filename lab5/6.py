import re

with open('row.txt', 'r') as file:
    data = file.read()

x = re.sub('[/s, /., /,]+', ':', data)
print(x)