from movies import movies

def isGood(mov):
    ans = []
    for i in mov:
        if i['imdb'] > 5.5:
            ans.append(i['name'])
    return ans

print(isGood(movies))