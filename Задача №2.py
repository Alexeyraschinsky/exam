def palindrome(s):
    return s[::-1]
while True:
    s = input('Введите слово палиндром:')
    print(f"{s} is palindrome!" if palindrome(s) else "not a palindrome")
    if s == 'n':
        break