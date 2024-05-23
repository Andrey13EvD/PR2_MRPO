from Repository import FakeRepository

class EquipmentRepository(FakeRepository.FakeRepository):

    def __init__(self):

        self._equip = []
    def add(self, equip):
        self._equip.append(equip)

    def remove(self, equip):
        if self._equip:
            for i in self._equip:
                if i.name == equip.name:
                    self._equip.remove(i)
    def get_all(self):
        return self._equip

    def get_by_name(self, equip):
        if self._equip:
            for i in self._equip:
                if i.name == equip:
                    return i
        return "Не найдено!"



