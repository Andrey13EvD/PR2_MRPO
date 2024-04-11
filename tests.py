import unittest
from datetime import datetime, timedelta

from TrainingProgram import TrainingProgram
from service_functions import add_exercise_to_program, check_equipment_availability, calculate_bmi, \
    get_user_recommendations, check_next_day_training_availability
from Exercises import Exercise
from Equipment import Equipment
from User import User



class TestServiceFunctions(unittest.TestCase):

    def test_add_exercise_to_program(self):
        program = TrainingProgram("Понедельник")
        exercise = Exercise("Приседания", [])
        add_exercise_to_program(exercise, program)
        self.assertIn(exercise, program.exercises)

    def test_check_equipment_availability(self):
        exercise = Exercise("Приседания", [])
        available_equipment = ["Гантели", "Штанга"]
        self.assertTrue(check_equipment_availability(exercise, available_equipment))

    def test_calculate_bmi(self):
        user = User("John", 30, 1.75, 75, "Сбросить вес", "Мужчина")
        self.assertAlmostEqual(calculate_bmi(user), 24.49, places=2)

    def test_get_user_recommendations_underweight(self):
        user = User("John", 30, 1.75, 55, "Сбросить вес", "Мужчина")
        self.assertEqual(get_user_recommendations(user), "Недостаточный вес. Рекомендуется увеличить прием калорий и проводить тренировки силового характера.")

    def test_get_user_recommendations_normal_weight(self):
        user = User("John", 30, 1.75, 70, "Сбросить вес", "Мужчина")
        self.assertEqual(get_user_recommendations(user), "Нормальный вес. Рекомендуется продолжать здоровый образ жизни.")

    def test_get_user_recommendations_overweight(self):
        user = User("John", 30, 1.75, 90, "Сбросить вес", "Мужчина")
        self.assertEqual(get_user_recommendations(user), "Избыточный вес. Рекомендуется уменьшить прием калорий и увеличить активность.")


    def test_add_existing_exercise(self):
        program = TrainingProgram("Понедельник")

        exercise = Exercise("Приседания", ["Гантели"])
        program.exercises.append(exercise)
        exercise_copy = Exercise("Приседания", ["Гантели"])

        with self.assertRaises(ValueError):
            add_exercise_to_program(exercise_copy, program)
        self.assertEqual(len(program.exercises), 1)

    def test_next_day_training_not_available(self):
        last_training_day = "Понедельник"
        current_day = "Вторник"
        self.assertFalse(check_next_day_training_availability(last_training_day, current_day))

if __name__ == '__main__':
    unittest.main()
