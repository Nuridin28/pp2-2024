def filter_prime(arr):
    sorted = []
    for i in arr:
        flag = True
        for j in range(2, int(i)):
            if int(i) % j == 0:
                flag = False
        if(flag and int(i) > 1):
            sorted.append(int(i))


    return sorted


x = list(input().split())

print(filter_prime(x))