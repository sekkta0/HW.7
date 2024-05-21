def is_palindrome(word):
    word = word.lower()
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True

word = input("Введіть слово: ")
if is_palindrome(word):
    print("Це слово - паліндром!")
else:
    print("Це слово - не паліндром.")
