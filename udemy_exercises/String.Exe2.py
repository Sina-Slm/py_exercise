# Given string contains a combination of the lower and upper case letters.
#  Write a program to arrange the characters of a string so that all lowercase letters should come first.

str1 = "PyNaTive"
str2, str3 = str(), str()
for letter in str1:
    if letter.islower():
        str2 += letter
    else:
        str3 += letter
print(str2 + str3)
