from Repository import FakeRepository

class MuscleGroupRepository(FakeRepository.FakeRepository):

    def __init__(self):

        self._mg = []
    def add(self, mg):
        self._mg.append(mg)

    def remove(self, mg):
        if self._mg:
            for i in self._mg:
                if i.name == mg.name:
                    self._mg.remove(i)
    def get_all(self):
        return self._mg

    def get_by_name(self, name):
        if self._mg:
            for i in self._mg:
                if i.name == name:
                    return i
        return "Не найдено!"



