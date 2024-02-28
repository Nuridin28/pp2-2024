import os
file = input()
if os.path.exists(file):
    if os.access(file, os.W_OK):
        os.remove(file)
        print('deleted')
    else :
        print('have no access')
else :
    print('file dont exists')