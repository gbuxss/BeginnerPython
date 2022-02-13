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


# print
'''
1
22
333
4444
55555
'''

i = 5
for x in range(1, i+1):
    for y in range(1, x+1):
        output = x * str(y)
    print(output)

