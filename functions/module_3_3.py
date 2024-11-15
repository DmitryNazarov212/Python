def print_params(a = 1,b = "строка",c = True):
    print(a,b,c)

# print_params(1,"не строка")
# print_params(b = 25)
# print_params(c = [1,2,3])


# values_list = [1,"string", False]
values_dict = {'a': 2, 'b': "строка", 'c': True}
# print_params(*values_list)
print_params(**values_dict)

# values_list_2 = [4, "vol"]
# print_params(*values_list_2, 42)