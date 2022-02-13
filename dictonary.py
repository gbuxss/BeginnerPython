# convert numbers into words e.g: 1234 -> one two three four
dict1 = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",

}

phone_num = input("phone:")
convert = ""
for num in phone_num:
    convert += dict1.get(num, '!!') + " "
print(convert)
