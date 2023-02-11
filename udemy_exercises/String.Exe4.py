# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all
# the characters in the s1 are present in s2. The character’s position doesn’t matter.

s1 = "Ynf"
s2 = "PYnative"
l1 = list()
[l1.append(char) for char in s1 if s2.count(char) > 0]
print(len(l1) == len(s1))
