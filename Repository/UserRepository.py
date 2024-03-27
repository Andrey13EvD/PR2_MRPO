from Repository import FakeRepository

class UserRepository(FakeRepository.FakeRepository):

    def __init__(self):

        self._user = []
    def add(self, user):
        self._user.append(user)

    def remove(self, user):
        if self._user:
            for i in self._user:
                if i.name == user.name:
                    self._user.remove(i)
    def get_all(self):
        return self._user

    def get_by_name(self, name):
        if self._user:
            for i in self._user:
                if i.name == name:
                    return i
        return "Пользователь не найден!"



