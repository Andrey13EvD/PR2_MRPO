from Repository import FakeRepository

class TrainingDayRepository(FakeRepository.FakeRepository):

    def __init__(self):

        self._tp = []
    def add(self, tp):
        self._tp.append(tp)

    def remove(self, tp):
        if self._tp:
            for i in self._tp:
                if i.weekDay == tp.weekDay:
                    self._tp.remove(i)
    def get_all(self):
        return self._tpr

    def get_by_name(self, weekDay):
        if self._tp:
            for i in self._tp:
                if i.weekDay == weekDay:
                    return i
        return "Не найдено!"



