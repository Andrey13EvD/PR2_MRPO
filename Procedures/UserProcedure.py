from Models import User
from Repository.UserRepository import UserRepository

class UserProcedure:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def add_user(self, user: User):
        if not self.user_repository.get_by_name(user.name):
            self.user_repository.add(user)
            print(f'Пользователь "{user.name}" успешно добавлен.')
        else:
            print(f'Пользователь "{user.name}" уже существует.')

    def remove_user(self, user_name: str):
        user = self.user_repository.get_by_name(user_name)
        if user != "Пользователь не найден!":
            self.user_repository.remove(user)
            print(f'Пользователь "{user_name}" успешно удален.')
        else:
            print(f'Пользователь "{user_name}" не найден.')

    def list_all_users(self):
        users_list = self.user_repository.get_all()
        if users_list:
            print('Список пользователей:')
            for user in users_list:
                print(f'Имя: {user.name}, Возраст: {user.age}, Рост: {user.height}, Вес: {user.weight}, Цель: {user.purpose}, Пол: {user.gender}')
        else:
            print('Список пользователей пуст.')

    def get_user_by_name(self, user_name: str):
        user = self.user_repository.get_by_name(user_name)
        if user != "Пользователь не найден!":
            print(f'Информация о пользователе "{user_name}":')
            print(f'Возраст: {user.age}, Рост: {user.height}, Вес: {user.weight}, Цель: {user.purpose}, Пол: {user.gender}')
        else:
            print(f'Пользователь "{user_name}" не найден.')

