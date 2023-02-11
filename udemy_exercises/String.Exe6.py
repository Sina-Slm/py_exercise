# Write a program to count occurrences of all characters within a string

str1 = "Apple is my favourite fruit"
out = dict()
for char in str1:
    out[char] = out.get(char, 0) + 1
print(out)
