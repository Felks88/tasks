import string


class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        for name_of_file in self.file_name:
            with open(name_of_file, 'r', encoding='utf-8') as file:
                i = file.read()
                i = i.lower()
                i = i.translate(str.maketrans('', '', string.punctuation))  # import string
                all_words[name_of_file] = i.split()
        return all_words

    def find(self, word):
        position = {}
        word = word.lower()
        for name_of_file in self.get_all_words().keys():
            for i in self.get_all_words().values():
                if word in i:
                    position[name_of_file] = i.index(word) + 1
                return position

    def count(self, word):
        number_of_words = {}
        word = word.lower()
        for name_of_file, i in self.get_all_words().items():  # Дошел до меня метод .items()
            if word in i:
                number_of_words[name_of_file] = i.count(word)
        return number_of_words


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
