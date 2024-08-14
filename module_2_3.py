my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
variable = 0
while variable < len(my_list):
    if my_list[variable] > 0:
        print(my_list[variable])
    elif my_list[variable] < 0:
        break
    variable = variable + 1
