my_list = [0,1,2,3,4,5,6,7,8,9]

list_comprehension = [x**2 for x in my_list]

generator_expression = (x**2 for x in my_list)


print(list_comprehension)

#print(generator_expression(my_list)) # doesn't work :(
print(generator_expression)