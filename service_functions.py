
from xml_repository import XMLRepository
from TrainingProgram import TrainingProgram
from Exercises import Exercise
from User import User

class TrainingProgramService:
    def __init__(self, xml_file):
        self.repository = XMLRepository(xml_file)

    def add_exercise_to_program(self, exercise_name, program_day):
        exercise = Exercise(exercise_name)
        program = TrainingProgram(program_day)
        self.repository.add_exercise_to_program(exercise, program)

    def check_equipment_availability(self, exercise, available_equipment):
        return self.repository.check_equipment_availability(exercise, available_equipment)

    def calculate_bmi(self, user_data):
        user = User(*user_data)
        return self.repository.calculate_bmi(user)

    def get_user_recommendations(self, user_data):
        user = User(*user_data)
        return self.repository.get_user_recommendations(user)

    def check_next_day_training_availability(self, last_training_day, current_day):
        return self.repository.check_next_day_training_availability(last_training_day, current_day)
