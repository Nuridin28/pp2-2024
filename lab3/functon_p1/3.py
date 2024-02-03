def solve(numheads, numlegs):
    rab = (numlegs - 2*numheads)/2
    chic = numheads - rab
    print(f'Numbers of rabbits is {rab} and numbers of chicken is {chic}')

heads = int(input())
legs = int(input())
solve(heads, legs)



'''
    x+y = 35
    2x+4y = 94
    2y = 24
    y = 12 x = 23
'''