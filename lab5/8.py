import re

with open('row.txt', 'r') as file:
    data = file.read()

x = re.split(r'(?=[A-Z])', data)
print(x)