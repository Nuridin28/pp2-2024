from movies import movies

def avg_imdb(mov):
    c = len(mov)
    sum = 0
    for i in mov:
        sum += i['imdb']
    return sum/c

print(avg_imdb(movies))