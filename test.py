import unittest
from Models.Equipment import Equipment
from Models.Exercise import Exercise
from Models.MuscleGroup import MuscleGroup
from Models.Recommendations import Recommendations
from Models.TrainingProgram import TrainingProgram
from Models.User import User

from business_rules import (
    validate_user_age, validate_user_gender, validate_user_weight, validate_user_height,
    validate_user_purpose, validate_exercise_repetitions, validate_exercise_assigned_to_training_program,
    #validate_equipment_assigned_to_exercise
)

class TestBusinessRules(unittest.TestCase):

    def setUp(self):
        self.equipment1 = Equipment(id=1, name="Гантели", description="Ручные грузы")
        self.exercise1 = Exercise(id=1, name="Приседания", description="Упражнение для ног", repetitions=10)
        self.muscle_group1 = MuscleGroup(id=1, name="Квадрицепсы", category="Ноги")
        self.recommendations1 = Recommendations(id=1, purpose="Похудение", recommendations="Соблюдайте диету и занимайтесь физическими упражнениями")
        self.training_program1 = TrainingProgram(id=1, week_day="Понедельник", exercises=[self.exercise1])
        self.user1 = User(id=1, age=30, gender="Мужчина", weight=75, height=1.75, name="John", purpose="Сбросить вес")

    def test_validate_user_age(self):
        self.assertTrue(validate_user_age(self.user1.age))
        self.assertFalse(validate_user_age(150))  # Неверный возраст

    def test_validate_user_gender(self):
        self.assertTrue(validate_user_gender(self.user1.gender))
        self.assertFalse(validate_user_gender("Other"))  # Неверный пол

    def test_validate_user_weight(self):
        self.assertTrue(validate_user_weight(self.user1.weight))
        self.assertFalse(validate_user_weight(400))  # Неверный вес

    def test_validate_user_height(self):
        self.assertTrue(validate_user_height(self.user1.height))
        self.assertFalse(validate_user_height(0.2))  # Неверный рост

    def test_validate_user_purpose(self):
        self.assertTrue(validate_user_purpose(self.user1.purpose))
        self.assertFalse(validate_user_purpose(""))  # Пустая цель

    def test_validate_exercise_repetitions(self):
        self.assertTrue(validate_exercise_repetitions(self.exercise1.repetitions))
        self.assertFalse(validate_exercise_repetitions(-10))  # Отрицательное количество повторений

    def test_validate_exercise_assigned_to_training_program(self):
        self.assertTrue(validate_exercise_assigned_to_training_program(self.training_program1, self.exercise1))
        self.assertFalse(validate_exercise_assigned_to_training_program(self.training_program1, Exercise(id=2, name="Пресс", description="Упражнение для пресса", repetitions=15)))  # Упражнение не назначено

#    def test_validate_equipment_assigned_to_exercise(self):
#        self.assertTrue(validate_equipment_assigned_to_exercise(self.equipment1, self.exercise1))
#        self.assertFalse(validate_equipment_assigned_to_exercise(Equipment(id=2, name="Брусья", description="Оборудование для отжиманий"), self.exercise1))  # Оборудование не используется

if __name__ == '__main__':
    unittest.main()
