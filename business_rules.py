from typing import List
from Models import Equipment, Exercise, MuscleGroup, Recommendations, TrainingProgram, User

# Бизнес-правила для User
def validate_user_age(age: int) -> bool:
    """Проверяет, что возраст пользователя в пределах от 0 до 120 лет."""
    return 0 <= age <= 120

def validate_user_gender(gender: str) -> bool:
    """Проверяет, что пол пользователя является либо 'Мужчина', либо 'Женщина'."""
    return gender in {"Мужчина", "Женщина"}

def validate_user_weight(weight: float) -> bool:
    """Проверяет, что вес пользователя в пределах от 0 до 300 кг."""
    return 0 <= weight <= 300

def validate_user_height(height: float) -> bool:
    """Проверяет, что рост пользователя в пределах от 0.5 до 2.5 метров."""
    return 50 <= height <= 250

def validate_user_purpose(purpose: str) -> bool:
    """Проверяет, что цель тренировок пользователя не пустая."""
    return bool(purpose)

# Бизнес-правила для Exercise
def validate_exercise_repetitions(repetitions: int) -> bool:
    """Проверяет, что количество повторений упражнения положительное и не превышает 1000."""
    return 0 < repetitions <= 1000

def validate_exercise_assigned_to_training_program(training_program: TrainingProgram, exercise: Exercise) -> bool:
    """Проверяет, что упражнение назначено тренировочной программе."""
    return exercise in training_program.exercises

