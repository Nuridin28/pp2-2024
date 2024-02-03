def convert_to_ounces(grams):
    return 28.3495231 * grams

gram = int(input())
x = convert_to_ounces(gram)
print(x)