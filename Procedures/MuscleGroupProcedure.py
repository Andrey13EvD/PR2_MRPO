from Models import MuscleGroup
from Repository.MuscleGroupRepository import MuscleGroupRepository

class MuscleGroupProcedure:
    def __init__(self, muscle_group_repository: MuscleGroupRepository):
        self.muscle_group_repository = muscle_group_repository

    def add_muscle_group(self, muscle_group: MuscleGroup):
        if not self.muscle_group_repository.get_by_name(muscle_group.name):
            self.muscle_group_repository.add(muscle_group)
            print(f'Мышечная группа "{muscle_group.name}" успешно добавлена.')
        else:
            print(f'Мышечная группа "{muscle_group.name}" уже существует.')

    def remove_muscle_group(self, muscle_group_name: str):
        muscle_group = self.muscle_group_repository.get_by_name(muscle_group_name)
        if muscle_group != "Не найдено!":
            self.muscle_group_repository.remove(muscle_group)
            print(f'Мышечная группа "{muscle_group_name}" успешно удалена.')
        else:
            print(f'Мышечная группа "{muscle_group_name}" не найдена.')

    def list_all_muscle_groups(self):
        muscle_groups_list = self.muscle_group_repository.get_all()
        if muscle_groups_list:
            for muscle_group in muscle_groups_list:
                print(f'ID: {muscle_group.id}, Название: {muscle_group.name}, Категория: {muscle_group.category}')
        else:
            print('Список мышечных групп пуст.')

    def get_muscle_group_info(self, muscle_group_name: str):
        muscle_group = self.muscle_group_repository.get_by_name(muscle_group_name)
        if muscle_group != "Не найдено!":
            info = muscle_group.get_info()
            print(f'Информация о мышечной группе "{muscle_group_name}": Название: {info[0]}, Категория: {info[1]}')
        else:
            print(f'Мышечная группа "{muscle_group_name}" не найдена.')

