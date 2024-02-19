import math
sides_count = int(input("Number of sides: "))
leng = int(input("Lenght of a side: "))
apothem = leng/2*math.tan(3.14/sides_count)

print("The area of the polygon is: ", round((sides_count*leng*apothem)/2))