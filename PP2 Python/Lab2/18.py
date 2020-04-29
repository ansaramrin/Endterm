def my_function(first_set, second_set,third_set):
     p=first_set.intersection(second_set) 
     res=p.union(third_set)
     return res
print(my_function({1, 2, 3, 4, 5}, {3, 5, 7},{8, 9, 10}))
