def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])
print_params()


values_list = ['Feliks', 1988, [9, 8]]
values_dict = {'a': 'дата', 'b': 1988, 'c': [9, 8]}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
