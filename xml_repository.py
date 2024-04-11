
from abc import ABC, abstractmethod
from lxml import etree
from User import User

class XMLRepository(ABC):
    def __init__(self, xml_file):
        self.xml_file = xml_file

    def add_exercise_to_program(self, exercise, program):
        # Открываем XML файл
        tree = etree.parse(self.xml_file)
        root = tree.getroot()

        # Создаем XML элемент для упражнения
        exercise_elem = etree.Element("exercise")
        exercise_elem.text = exercise.name

        # Добавляем упражнение в программу тренировок
        for day in root.findall(".//day"):
            if day.attrib["name"] == program.day:
                day.append(exercise_elem)

        # Сохраняем изменения в XML файл
        tree.write(self.xml_file, pretty_print=True)

    def check_equipment_availability(self, exercise, available_equipment):
        # Проверяем доступность оборудования для упражнения
        required_equipment = exercise.required_equipment
        for eq in required_equipment:
            if eq not in available_equipment:
                return False
        return True

    def calculate_bmi(self, user):
        # Расчет индекса массы тела пользователя
        return user.weight / (user.height ** 2)

    def get_user_recommendations(self, user):
        # Получение рекомендаций для пользователя
        bmi = self.calculate_bmi(user)
        if bmi < 18.5:
            return "Недостаточный вес. Рекомендуется увеличить прием калорий и проводить тренировки силового характера."
        elif 18.5 <= bmi < 25:
            return "Нормальный вес. Рекомендуется продолжать здоровый образ жизни."
        else:
            return "Избыточный вес. Рекомендуется уменьшить прием калорий и увеличить активность."

    def check_next_day_training_availability(self, last_training_day, current_day):
        # Проверка на отдых между днями тренировок
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        last_training_index = days_of_week.index(last_training_day)
        current_index = days_of_week.index(current_day)
        return (current_index - last_training_index) % len(days_of_week) != 1
