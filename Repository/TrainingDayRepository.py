from Repository import FakeRepository

class trainingDayRepository(FakeRepository.FakeRepository):

    def __init__(self):

        self._td = []
    def add(self, td):
        self._td.append(td)

    def remove(self, td):
        if self._td:
            for i in self._td:
                if i.name == td.name:
                    self._td.remove(i)
    def get_all(self):
        return self._td

    def get_by_name(self, name):
        if self._td:
            for i in self._td:
                if i.name == name:
                    return i
        return "Не найден!"



