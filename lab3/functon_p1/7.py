def has_33(nums):
    for i in range(0, len(nums) - 1):
        if int(nums[i]) == 3:
            if int(nums[i+1]) == 3:
                return True
    return False

x = list(input().split())
print(has_33(x))