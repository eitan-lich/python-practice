import time

# selected_sentence = "hello this is a sample sentence to test how many times each letter appears"
#
# letter_count = {}
#
# for letter in selected_sentence:
#     if letter not in letter_count.keys():
#         letter_count[letter] = 1
#     else:
#         letter_count[letter] += 1
#
# print(letter_count)
#

desired_colum = 3
desired_row = 2

matrix = [
    [2, 5 ,213],
    [23, 12, 5],
    [43, 14 ,6],
    [23, 12, 5353],
    [43,123,]
]

# print([ column for column in matrix for row in matrix ])

# rev = "hello"
# print(rev[::-1])
#
# nums = [43,2134,34,423,123]
# copy = nums[::]
# copy[0] = 423
# print(nums[0])
# copy.append((23,213))
# print(copy)
#

print({time.time(): num+1 for num in range(1,10)})
print(list(range(1,10, 5)))
