import os

print('Exists:', os.access('js.json', os.F_OK))
print('Readable:', os.access('js.json', os.R_OK))
print('Writable:', os.access('js.json', os.W_OK))
print('Executable:', os.access('js.json', os.X_OK))