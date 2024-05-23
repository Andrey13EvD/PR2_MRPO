#from business_rules import validate_equipment_assigned_to_exercise
from Models import Equipment, Exercise
from Repository.EquipmentRepository import EquipmentRepository

class EquipmentProcedure:
    def __init__(self, equipment_repository: EquipmentRepository):
        self.equipment_repository = equipment_repository

    def add_equipment(self, equipment: Equipment):
        if not self.equipment_repository.get_by_name(equipment.name):
            self.equipment_repository.add(equipment)
            print(f'Оборудование "{equipment.name}" успешно добавлено.')
        else:
            print(f'Оборудование "{equipment.name}" уже существует.')

    def remove_equipment(self, equipment_name: str):
        equipment = self.equipment_repository.get_by_name(equipment_name)
        if equipment != "Не найдено!":
            self.equipment_repository.remove(equipment)
            print(f'Оборудование "{equipment_name}" успешно удалено.')
        else:
            print(f'Оборудование "{equipment_name}" не найдено.')

    def list_all_equipment(self):
        equipment_list = self.equipment_repository.get_all()
        if equipment_list:
            for equipment in equipment_list:
                print(f'ID: {equipment.id}, Название: {equipment.name}, Описание: {equipment.description}')
        else:
            print('Список оборудования пуст.')

    def assign_equipment_to_exercise(self, equipment_name: str, exercise: Exercise):
        equipment = self.equipment_repository.get_by_name(equipment_name)
        if equipment != "Не найдено!" and validate_equipment_assigned_to_exercise(equipment, exercise):
            exercise.required_equipment.append(equipment.name)
            print(f'Оборудование "{equipment_name}" успешно назначено упражнению "{exercise.name}".')
        else:
            print(f'Не удалось назначить оборудование "{equipment_name}" упражнению "{exercise.name}". Возможно, оборудование уже назначено или не существует.')
