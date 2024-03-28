from datetime import timedelta

from Exercises import Exercise
from Equipment import Equipment
from User import User

# Добавление упражнения в тренировочную программу
def add_exercise_to_program(exercise, program):
    program.exercises.append(exercise)

# Проверка доступности оборудования для упражнения
def check_equipment_availability(exercise, available_equipment):
    required_equipment = exercise.required_equipment
    for eq in required_equipment:
        if eq not in available_equipment:
            return False
    return True

# Расчет индекса массы тела пользователя
def calculate_bmi(user):
    return user.weight / (user.height ** 2)

# Получение рекомендаций для пользователя
def get_user_recommendations(user):
    bmi = calculate_bmi(user)
    if bmi < 18.5:
        return "Недостаточный вес. Рекомендуется увеличить прием калорий и проводить тренировки силового характера."
    elif 18.5 <= bmi < 25:
        return "Нормальный вес. Рекомендуется продолжать здоровый образ жизни."
    else:
        return "Избыточный вес. Рекомендуется уменьшить прием калорий и увеличить активность."

#Проверка на дублирование упражнений в один тренировочный день
def add_exercise_to_program(exercise, program):
    if exercise not in program.exercises:
        program.exercises.append(exercise)
    else:
        raise ValueError("Упражнение уже добавлено в программу тренировок")

#Проверка на перетренированность. Нельзя ставить тренировки два дня подряд
def check_next_day_training_availability(last_training_day, current_day):
    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    last_training_index = days_of_week.index(last_training_day)
    current_index = days_of_week.index(current_day)
    return (current_index - last_training_index) % len(days_of_week) != 1




