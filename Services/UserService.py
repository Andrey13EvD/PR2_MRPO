from Models.Equipment import Equipment
from Models.Exercise import Exercise
from Models.MuscleGroup import MuscleGroup
from Models.Recommendations import Recommendations
from Models.TrainingProgram import TrainingProgram
from Models.User import User
from Repository.XMLRepository import XMLEquipmentRepository, XMLExerciseRepository, XMLMuscleGroupRepository, \
    XMLRecommendationsRepository, XMLTrainingProgramRepository, XMLUserRepository

class UserService:
    def __init__(self, user_repository: XMLUserRepository,
                 equipment_repository: XMLEquipmentRepository,
                 exercise_repository: XMLExerciseRepository,
                 muscle_group_repository: XMLMuscleGroupRepository,
                 recommendations_repository: XMLRecommendationsRepository,
                 training_program_repository: XMLTrainingProgramRepository):
        self.user_repository = user_repository
        self.equipment_repository = equipment_repository
        self.exercise_repository = exercise_repository
        self.muscle_group_repository = muscle_group_repository
        self.recommendations_repository = recommendations_repository
        self.training_program_repository = training_program_repository

    def add_user(self, user: User):
        self.user_repository.add(user)

    def get_user_by_id(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def get_all_users(self):
        return self.user_repository.get_all()

    def add_equipment_to_user(self, user_id, equipment: Equipment):
        user = self.user_repository.get_by_id(user_id)
        if user:
            self.equipment_repository.add(equipment)
            user.equipment.append(equipment)
            self.user_repository.update(user)
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def add_exercise_to_user(self, user_id, exercise: Exercise):
        user = self.user_repository.get_by_id(user_id)
        if user:
            self.exercise_repository.add(exercise)
            user.exercises.append(exercise)
            self.user_repository.update(user)
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def add_muscle_group_to_user(self, user_id, muscle_group: MuscleGroup):
        user = self.user_repository.get_by_id(user_id)
        if user:
            self.muscle_group_repository.add(muscle_group)
            user.muscle_groups.append(muscle_group)
            self.user_repository.update(user)
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def add_recommendations_to_user(self, user_id, recommendations: Recommendations):
        user = self.user_repository.get_by_id(user_id)
        if user:
            self.recommendations_repository.add(recommendations)
            user.recommendations.append(recommendations)
            self.user_repository.update(user)
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def add_training_program_to_user(self, user_id, training_program: TrainingProgram):
        user = self.user_repository.get_by_id(user_id)
        if user:
            self.training_program_repository.add(training_program)
            user.training_programs.append(training_program)
            self.user_repository.update(user)
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def get_all_equipment_for_user(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        if user:
            return user.equipment
        else:
            return f"Пользователь с ID {user_id} не найден."

    def get_all_exercises_for_user(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        if user:
            return user.exercises
        else:
            return f"Пользователь с ID {user_id} не найден."

    def get_all_muscle_groups_for_user(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        if user:
            return user.muscle_groups
        else:
            return f"Пользователь с ID {user_id} не найден."

    def get_all_recommendations_for_user(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        if user:
            return user.recommendations
        else:
            return f"Пользователь с ID {user_id} не найден."

    def get_all_training_programs_for_user(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        if user:
            return user.training_programs
        else:
            return f"Пользователь с ID {user_id} не найден."