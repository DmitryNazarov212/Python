import time
class User:
    def __init__(self, nickname= ' ', password = ' ', age = 0):
        self.__nickname = nickname
        self.__password = hash(password)
        self.__age = age
    @property  
    def nickname(self):  
        return self.__nickname
    @property  
    def password(self):  
        return self.__password
    @property  
    def age(self):  
        return self.__age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.__title_ = title
        self.__duration_ = duration
        self.__time_now_ = time_now
        self.__adult_mode_ = adult_mode
    
    @property  
    def title(self):  
        return self.__title_
    @property  
    def duration(self):  
        return self.__duration_
    @property  
    def time_now(self):  
        return self.__time_now_ 
    @property  
    def adult_mode(self):  
        return self.__adult_mode_

class UrTube:
    users = []
    videos = []
    counter = 0
    def __init__(self, current_user = None, current_user_number = 0):
        self.current_user = current_user
        self.current_user_number_ = current_user_number
    
    def log_in(self, nickname, password):
       for i in range(len(self.users)):
            if nickname == self.users[i].nickname and hash(password) == self.users[i].password:
                print(f"Добро пожаловать {nickname}!")
                self.current_user = nickname
                self.current_user_number_ = i
                break

    def register(self, nickname, password, age):
        for user in self.users:  
            if user.nickname == nickname:  
                print(f"Пользователь {nickname} уже существует")  
                return 
        self.users.append(User(nickname, password, age))  
        print(f'Пользователь {nickname} зарегистрирован!')  
        
        self.counter += 1  
        self.log_in(nickname, password)  # Выполняем вход после регистраци

    def log_out(self):
        print("Вы вышли из аккаунта")
        self.current_user = None
        self.current_user_number_ = 0

    def add(self,*args):
        for item in args:
            self.videos.append(item)
    
    def get_videos(self, search):
        found = []
        for i in range(len(self.videos)):
            if search.lower() in self.videos[i].title.lower():
                found.append(self.videos[i].title)
        return found
    
    def watch_video(self, searched_string):
        if(self.current_user == None):
            print("Войдите в аккаунт, чтобы смотреть видео")
            return 
        for i in range(len(self.videos)):
            if searched_string == self.videos[i].title:
                if(self.videos[i].adult_mode == True and self.users[self.current_user_number_].age < 18):
                    print("Вам нет 18 лет, пожалуйста покиньте страницу!")
                    return
                for second in range(self.videos[i].duration):  
                    print(f"{second + 1} ", end='', flush=True)
                    time.sleep(1)
                print("Конец видео")
                

        
        

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
    # ur = UrTube()

    # v1 = Video('Лучший язык программирования 2024 года', 200)
    # v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    # ur.add(v1, v2)
    # print(ur.get_videos('лучший'))

    # ur.watch_video('Для чего девушкам парень программист?')
    # while(True):
    #     cmd = int(input("Введите команду:"))
    #     if cmd == 1:
    #         ur.register(nickname:= input("Введите никнейм: "), password:= input("Введите пароль: "), age:=input("Введите свой возраст: "))
    #     if cmd == 2:
    #         ur.log_in(nickname:= input("Введите никнейм: "),password1:= input("Введите пароль: "))
            

        

        