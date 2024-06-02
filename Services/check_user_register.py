from DB.DBModels import User
from Repository.UserRepository import UserRepository

class CheckUserRegister:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def _check_user_register(self, user_id: int) -> bool:
        return self.user_repository.get_by_id(user_id) is not None

    def execute(self, user_id: int) -> bool:
        return self._check_user_register(user_id)

# Пример использования
if __name__ == "__main__":
    user_repo = UserRepository()
    checker = CheckUserRegister(user_repo)

    # Пример проверки пользователя с ID = 1
    user_id = 1
    is_registered = checker.execute(user_id)
    if is_registered:
        print(f"Пользователь с ID {user_id} зарегистрирован.")
    else:
        print(f"Пользователь с ID {user_id} не зарегистрирован.")