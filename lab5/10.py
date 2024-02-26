import re

with open('row.txt', 'r') as file:
    data = file.read()

x = re.sub('([a-z])([A-Z])', '\\1_\\2', data).lower()
print(x)