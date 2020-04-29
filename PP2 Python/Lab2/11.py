def my_function(first_set, second_set):
    first_set.difference_update(second_set)
    return first_set

print(my_function({1, 2, 3, 4}, {3, 5, 7}))
print(my_function({12, 15, 16, 20, 95}, {1, 2, 3, 16, 17, 20}))
