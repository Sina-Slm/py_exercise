# Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt.
# Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt
# will contain letter b, and so on.

import string
letters = string.ascii_lowercase
letter_list = list()

for i in range(26):
    with open(f"letter/{letters[i]}.txt", "r") as file:
        text = file.read()
        letter_list.append(text)
print(letter_list)
