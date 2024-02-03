from movies import movies

def avg_imdb_by_cat(mov, cat):
    c = 0
    sum = 0
    for i in mov:
        if i['category'] == cat:
            sum += i['imdb']
            c += 1
    return sum/c
cat = input('Write a category: ')
print(avg_imdb_by_cat(movies, cat))