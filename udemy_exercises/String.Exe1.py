# Given two strings, s1 and s2, write a program to return a new string
#  made of s1 and s2’s first, middle, and last characters.

s1, s2 = "America", "Japan"
s3, z = list(), str()
a = [s[0] + s[(len(s))//2] + s[-1] for s in [s1, s2]]
for i in range(3):
    z = z + a[0][i] + a[1][i]
print(z)
