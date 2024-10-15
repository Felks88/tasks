def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        try:
            result[i.__name__] = i(int_list)
        except TypeError:
            pass
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
