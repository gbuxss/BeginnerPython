# print following:
'''print following in output
XXXXX
XX
XXXXX
XX
XX
'''

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ''
    for count in range(number):
        output += 'X'
    print(output)


