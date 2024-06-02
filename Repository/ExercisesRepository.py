from Repository import FakeRepository

class ExercisesRepository(FakeRepository.FakeRepository):

    def __init__(self):

        self._exer = []
    def add(self, exer):
        self._exer.append(exer)

    def remove(self, exer):
        if self._exer:
            for i in self._exer:
                if i.name == exer.name:
                    self._exer.remove(i)
    def get_all(self):
        return self._exer

    def get_by_name(self, name):
        if self._exer:
            for i in self._exer:
                if i.name == name:
                    return i
        return "Не найдено!"

    def get_by_id(self, id):
        if self._exer:
            for i in self._exer:
                if i.id == id:
                    return i
        return "Не найдено!"



