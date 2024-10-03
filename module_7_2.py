import io


def custom_write(file_name, strings):
    strings_position = {}
    file = open(file_name, "w", encoding="utf-8")
    for i in strings:
        start_str = file.tell()
        file.write(i + "\n")
        strings_position[(len(strings_position) + 1, start_str)] = i
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
