#list,set,dictionaries are muttable
def my_function(my_tuple):
    for i in my_tuple:
        if type(i) == list:
            return True
        elif type(i) == set:
            return True
        elif type(i) == dict:
            return True
    return False
print(my_function((10, 2, 5, [4, 8, 2], 3, 5)))
print(my_function((5, 2.5, 8, 4, 'Hi', -5, True, 6)))
