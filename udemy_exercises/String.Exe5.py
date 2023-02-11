# Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?".lower()
counter, i = 0, 0
for char in str1:
    if char == "u" and str1[i+1] == "s" and str1[i+2] == "a":
        counter += 1
    i += 1
print(counter)
