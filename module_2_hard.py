def pas (num):
    pas = ''
    for i in range(1, num):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                pas = pas + str(i) + str(j) #не сложить, а составить
    return pas
print('Введите число, выпавшее на камне: ')
print('Скорее пиши это на втором камне:', pas(int(input())))

