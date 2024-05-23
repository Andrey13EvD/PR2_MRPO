from business_rules import validate_exercise_repetitions
from Models import Exercise, TrainingProgram
from Repository.ExercisesRepository import ExercisesRepository

class ExerciseProcedure:
    def __init__(self, exercises_repository: ExercisesRepository):
        self.exercises_repository = exercises_repository

    def add_exercise(self, exercise: Exercise):
        if not self.exercises_repository.get_by_name(exercise.name):
            if validate_exercise_repetitions(exercise.repetitions):
                self.exercises_repository.add(exercise)
                print(f'Упражнение "{exercise.name}" успешно добавлено.')
            else:
                print(f'Некорректное количество повторений для упражнения "{exercise.name}".')
        else:
            print(f'Упражнение "{exercise.name}" уже существует.')

    def remove_exercise(self, exercise_name: str):
        exercise = self.exercises_repository.get_by_name(exercise_name)
        if exercise != "Не найдено!":
            self.exercises_repository.remove(exercise)
            print(f'Упражнение "{exercise_name}" успешно удалено.')
        else:
            print(f'Упражнение "{exercise_name}" не найдено.')

    def list_all_exercises(self):
        exercises_list = self.exercises_repository.get_all()
        if exercises_list:
            for exercise in exercises_list:
                print(f'ID: {exercise.id}, Название: {exercise.name}, Описание: {exercise.description}, Повторения: {exercise.repetitions}')
        else:
            print('Список упражнений пуст.')

    def assign_exercise_to_training_program(self, training_program: TrainingProgram, exercise_name: str):
        exercise = self.exercises_repository.get_by_name(exercise_name)
        if exercise != "Не найдено!":
            if exercise not in training_program.exercises:
                training_program.exercises.append(exercise)
                print(f'Упражнение "{exercise_name}" успешно назначено тренировочной программе "{training_program.week_day}".')
            else:
                print(f'Упражнение "{exercise_name}" уже назначено тренировочной программе "{training_program.week_day}".')
        else:
            print(f'Упражнение "{exercise_name}" не найдено.')