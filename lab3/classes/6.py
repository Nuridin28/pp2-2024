import math
my_list = []

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

new_list = list(filter(lambda x: (isPrime(x)) , my_list))
print(new_list)