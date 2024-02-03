from movies import movies

def isGood(mov):
    if mov['imdb'] > 5.5:
        return True
    return False
x = int(input('Введите номер фильма '))
print(isGood(movies[x]))