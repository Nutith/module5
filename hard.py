from time import sleep


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        log_in_error = True

        if nickname in self.users:
            log_in_error = False

        if not log_in_error:
            user = self.users[self.users.index(nickname)]
            if hash(password) != user.password:
                log_in_error = True

        if log_in_error:
            print('Ошибка в имени пользователя или пароле')
            return

        self.current_user = user

    def register(self, nickname, password, age):
        user = User(nickname, hash(password), age)

        if user in self.users:
            print(f'Пользователь {nickname} уже существует')
            return

        self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        [self.videos.append(x) for x in args if x not in self.videos]

    def get_videos(self, request):
        return [x.title for x in self.videos if request in x]

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        if title not in self.videos:
            return

        video = self.videos[self.videos.index(title)]

        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return

        for i in range(1, video.duration+1):
            print(i, end=' ')
            video.time_now = i
            sleep(0.2)

        print('Конец видео')
        video.time_now = 0


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.time_now = 0
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title

    def __str__(self):
        return f'"{self.title}", {self.duration} минут' + (' 18+' if self.adult_mode else '')

    def __eq__(self, other):
        if isinstance(other, Video):
            return other.title == self.title
        elif isinstance(other, str):
            return other == self.title

    def __contains__(self, item):
        return item.lower() in self.title.lower()


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'{self.nickname}, {self.age}'

    def __eq__(self, other):
        if isinstance(other, User):
            return other.nickname == self.nickname
        elif isinstance(other, str):
            return other == self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 11)

# Добавление видео
ur.add(v1, v2)
ur.add(v3)

print('Полный список видео:')
[print(x) for x in ur.videos]
print()

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('charlie', 'suppwd123', 25)
ur.log_out()

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.log_in('cha', 'cha')
ur.log_in('charlie', 'suppwd123')
print(ur.current_user)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
