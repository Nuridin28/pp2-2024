import shutil
def cop():
    f = input()
    s = input()
    shutil.copyfile(f'{f}.txt', f'{s}.txt')

cop()