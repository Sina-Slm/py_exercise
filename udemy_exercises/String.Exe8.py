# Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician"
str2 = str()
for char in str1:
    if char.isalnum() or (char.isspace() and not str2[-1].isspace()):
        str2 += char
print(str2)
