from Repository import FakeRepository

class RecommendationsRepository(FakeRepository.FakeRepository):

    def __init__(self):

        self._rec = []
    def add(self, rec):
        self._rec.append(rec)

    def remove(self, rec):
        if self._rec:
            for i in self._rec:
                if i.purpose == rec.recommendations:
                    self._rec.remove(i)
    def get_all(self):
        return self._rec

    def get_by_name(self, recommendations):
        if self._rec:
            for i in self._rec:
                if i.recommendations == recommendations:
                    return i
        return "Не найдено!"



