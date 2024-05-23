from Models import TrainingProgram
from Repository.TrainingProgramRepository import TrainingProgramRepository

class TrainingProgramProcedure:
    def __init__(self, training_program_repository: TrainingProgramRepository):
        self.training_program_repository = training_program_repository

    def add_training_program(self, training_program: TrainingProgram):
        if not self.training_program_repository.get_by_id(training_program.id):
            self.training_program_repository.add(training_program)
            print(f'Тренировочная программа с ID {training_program.id} успешно добавлена.')
        else:
            print(f'Тренировочная программа с ID {training_program.id} уже существует.')

    def remove_training_program(self, training_program_id: int):
        training_program = self.training_program_repository.get_by_id(training_program_id)
        if training_program:
            self.training_program_repository.remove(training_program)
            print(f'Тренировочная программа с ID {training_program_id} успешно удалена.')
        else:
            print(f'Тренировочная программа с ID {training_program_id} не найдена.')

    def list_all_training_programs(self):
        training_programs_list = self.training_program_repository.get_all()
        if training_programs_list:
            print('Список тренировочных программ:')
            for training_program in training_programs_list:
                print(f'ID: {training_program.id}, День недели: {training_program.week_day}')
        else:
            print('Список тренировочных программ пуст.')

    def get_training_program_by_id(self, training_program_id: int):
        training_program = self.training_program_repository.get_by_id(training_program_id)
        if training_program:
            print(f'Информация о тренировочной программе с ID {training_program_id}:')
            print(f'День недели: {training_program.week_day}')
            print(f'Упражнения: {", ".join([exercise.name for exercise in training_program.exercises])}')
        else:
            print(f'Тренировочная программа с ID {training_program_id} не найдена.')
