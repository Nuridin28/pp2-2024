from itertools import permutations 
def perm(s):
    per = permutations(s) 
    for i in per: 
        for j in i:
            print(j, end = '')
        print('')
        
s = input()
perm(s)