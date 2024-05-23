import os
from Models.User import User
from Models.Equipment import Equipment
from Models.Recommendations import Recommendations
from Models.Exercise import Exercise
from Models.MuscleGroup import MuscleGroup
from Models.TrainingProgram import TrainingProgram
from Repository.XMLRepository import (XMLUserRepository, XMLEquipmentRepository, XMLRecommendationsRepository,
                                      XMLExerciseRepository, XMLMuscleGroupRepository, XMLTrainingProgramRepository)
def populate_user_repository(file_path):
    user_repo = XMLUserRepository(file_path)
    users = [
        User(id=1, age=25, gender="Мужчина", weight=70.5, height=175, name="Иван Иванов", purpose="Увеличение мышечной массы"),
        User(id=2, age=30, gender="Женщина", weight=60.0, height=165, name="Анна Иванова", purpose="Снижение веса")
    ]
    for user in users:
        user_repo.add(user)


def populate_equipment_repository(file_path):
    equipment_repo = XMLEquipmentRepository(file_path)
    equipments = [
        Equipment(id=1, name="Гантели", description="Короткая штанга с грузиками на каждом конце"),
        Equipment(id=2, name="Беговая дорожка", description="Приспособление для ходьбы или бега при нахождении на одном месте")
    ]
    for equipment in equipments:
        equipment_repo.add(equipment)


def populate_recommendations_repository(file_path):
    recommendations_repo = XMLRecommendationsRepository(file_path)
    recommendations = [
        Recommendations(id=1, purpose="Снижение веса", recommendations="Кардиотренировки и сбалансированное питание"),
        Recommendations(id=2, purpose="Увеличение мышечной массы", recommendations="Силовые тренировки и высокое потребление белка")
    ]
    for recommendation in recommendations:
        recommendations_repo.add(recommendation)


def populate_exercise_repository(file_path):
    exercise_repo = XMLExerciseRepository(file_path)
    exercises = [
        Exercise(id=1, name="Подтягивания", description="Обычное гимнастическое упражнение", repetitions=15),
        Exercise(id=2, name="Приседания", description="Упражнение на ноги", repetitions=20)
    ]
    for exercise in exercises:
        exercise_repo.add(exercise)


def populate_muscle_group_repository(file_path):
    muscle_group_repo = XMLMuscleGroupRepository(file_path)
    muscle_groups = [
        MuscleGroup(id=1, name="Грудные мышцы", category="Грудь"),
        MuscleGroup(id=2, name="Квадрицепсы", category="Ноги")
    ]
    for muscle_group in muscle_groups:
        muscle_group_repo.add(muscle_group)


def populate_training_program_repository(file_path):
    training_program_repo = XMLTrainingProgramRepository(file_path)
    exercises = [
        Exercise(id=1, name="Подтягивания", description="Обычное гимнастическое упражнение", repetitions=15),
        Exercise(id=2, name="Приседания", description="Упражнение на ноги", repetitions=20)
    ]
    training_programs = [
        TrainingProgram(id=1, week_day="Понедельник", exercises=exercises),
        TrainingProgram(id=2, week_day="Среда", exercises=exercises)
    ]
    for program in training_programs:
        training_program_repo.add(program)


def main():
    if not os.path.exists('data'):
        os.makedirs('data')

    populate_user_repository('data/users.xml')
    populate_equipment_repository('data/equipment.xml')
    populate_recommendations_repository('data/recommendations.xml')
    populate_exercise_repository('data/exercises.xml')
    populate_muscle_group_repository('data/muscle_groups.xml')
    populate_training_program_repository('data/training_programs.xml')

    print("Заполнение данных завершено.")


if __name__ == "__main__":
    main()
