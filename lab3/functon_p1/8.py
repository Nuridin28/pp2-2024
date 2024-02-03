def spy_game(nums):
    ans = []
    for i in nums:
        if int(i) == 0 or int(i) == 7:
            ans.append(int(i))
    for i in range(0, len(ans) - 2):
        if ans[i] == 0:
            if ans[i+1] == 0:
                if ans[i+2] == 7:
                    return True

    return False
#x = list(input().split(',')) Если принимаем через запятую
x = list(input().split())
print(spy_game(x))