# Write a program to find words with both alphabets and numbers from an input string.

str1 = "Emma25 is Data scientist50 and AI Expert"
str1 = str1.split()
str2 = list()
for item in str1:
    if any(char.isalpha for char in item) and any(char.isdigit() for char in item):
        str2.append(item)
print(str2)
