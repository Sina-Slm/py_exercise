# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
for item in str_list:
    if not item:
        str_list.remove(item)
print(str_list)        