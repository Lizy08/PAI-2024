def is_palindrome(s):
    return s == s[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome!")
