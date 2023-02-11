# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"
chars, digits, symbols = 0, 0, 0
for letter in str1:
    if letter.isalpha():
        chars += 1
    elif letter.isdigit():
        digits += 1
    elif not letter.isalnum():
        symbols += 1
print(f"chars = {chars}\ndigits = {digits}\nsymbols = {symbols}")
