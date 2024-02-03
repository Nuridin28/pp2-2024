from movies import movies

def categor(mov, cat):
    ans = []
    for i in mov:
        if i['category'] == cat:
            ans.append(i['name'])
    return ans
cat = input("Write a category: ")
print(categor(movies, cat))