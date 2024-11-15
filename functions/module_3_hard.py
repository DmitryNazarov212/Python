new_container = []
def recursion(*args):
    for elements in args:
        if isinstance(elements, (list, tuple, set)):
            recursion(*elements)
        else:
            new_container.append(elements)
    return new_container

def calculate_structure_sum(*args):
    my_sum = 0
    correct_list = []
    correct_list = recursion(*args)
    for i in range(len(correct_list)):
        if isinstance(correct_list[i], str):
            my_sum += len(correct_list[i])
        elif  type(correct_list[i]) == dict:
            for key in correct_list[i].keys():
                my_sum += correct_list[i][key] + len(key)
        else:
            my_sum += correct_list[i]
    return my_sum




data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)