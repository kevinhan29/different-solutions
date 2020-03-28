'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6), ('fourth_element', 1), \
                 ('fifth_element', 8), ('sixth_element', 5), ('seventh_element', 0)]
sorted_list = []
# make sorted_list same length as unsorted_list
for x in unsorted_list:
    sorted_list.append(0)
    # print(x)
    # print(sorted_list)

# create a list using only the number values in unsorted_list and sort the list
num_list = [x[1] for x in unsorted_list]
num_list.sort()
# print(num_list)

# iterate through unsorted_list objects
for x in unsorted_list:
    for y in num_list:      # iterate through num_list and compare with number value in sorted_list
        if y == x[1]:       # if there is a match, add the tuple to sorted_list in the same index position of the match
            n = num_list.index(y)
            # print(n)
            sorted_list[n] = x
            num_list[n] = "EMPTY"     # replace used number so it doesn't get re-used
            # print(num_list)

print(sorted_list)
