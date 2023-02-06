# Create a function that takes a text file as input and returns the number of words contained in the text file.
# Please take into consideration that a comma can separate some words with no space. For example, "Hi,it's me."
#  would need to be counted as three words. For your convenience, you can use the text file in the attachment.

def WordsFun(txtfile):
    sen = list()
    with open(txtfile, 'r') as file:
        text = file.read()
        text_list = text.strip().split()
        [sen.extend(word.split(",")) for word in text_list]
        return len(sen)

print(WordsFun('word1.txt'))
