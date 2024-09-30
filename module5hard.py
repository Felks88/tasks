import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.password == other.password

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []  # список Userов
        self.videos = []  # список Video
        self.current_user = None  # текущий пользователь

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and password == i.password:
                self.current_user = i

    def register(self, nickname, password, age):
        for i in self.users:
            if nickname == i.nickname:
                print(f'Пользователь {nickname} уже зарегистрирован')
                return
        i = User(nickname, password, age)
        self.users.append(i)
        self.current_user = i

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for i in videos:
            if i not in self.videos:
                self.videos.append(i)

        else:
            pass

    def get_videos(self, request):
        list_title = []
        for i in self.videos:
            if request.lower() in i.title.lower():
                list_title.append(i.title)
        return list_title

    def watch_video(self, title):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for i in self.videos:
                if title in i.title:
                    for j in range(1, 11):
                        print(j, end=' ')
                        time.sleep(0.25)  # для ускорения проверки
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
