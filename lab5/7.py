import re

with open('row.txt', 'r') as file:
    data = file.read()

x = re.sub('_([a-zA-Z])',lambda x: x.group(1).upper(), data )
print(x)