def isPalin(s):
    if s == s[::-1]:
        print('Palindrome')
    else:
        print("Not a palindrome")

s = input()
isPalin(s)