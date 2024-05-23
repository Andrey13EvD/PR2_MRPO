from Models.MuscleGroup import MuscleGroup
from Models import User, Exercise, Equipment, MuscleGroup, TrainingProgram, Recommendations
from Procedures.EquipmentProcedure import EquipmentProcedure
from Procedures.ExerciseProcedure import ExerciseProcedure
from Procedures.UserProcedure import UserProcedure
from Procedures.TrainingProgramProcedure import TrainingProgramProcedure
from Procedures.RecommendationsProcedure import RecommendationsProcedure
from Procedures.MuscleGroupProcedure import MuscleGroupProcedure
from Repository.XMLRepository import (XMLExerciseRepository, XMLEquipmentRepository, XMLUserRepository,
                                      XMLMuscleGroupRepository, XMLRecommendationsRepository, XMLTrainingProgramRepository)
from Services.UserService import UserService

# Инициализация репозиториев
user_repository = XMLUserRepository('data/users.xml')
equipment_repository = XMLEquipmentRepository('data/equipment.xml')
exercises_repository = XMLExerciseRepository('data/exercises.xml')
muscle_groups_repository = XMLMuscleGroupRepository('data/muscle_groups.xml')
recommendations_repository = XMLRecommendationsRepository('data/recommendations.xml')
training_programs_repository = XMLTrainingProgramRepository('data/training_programs.xml')

# Инициализация процедур и сервиса
user_procedure = UserProcedure(user_repository)
equipment_procedure = EquipmentProcedure(equipment_repository)
exercises_procedure = ExerciseProcedure(exercises_repository)
muscle_groups_procedure = MuscleGroupProcedure(muscle_groups_repository)
training_programs_procedure = TrainingProgramProcedure(training_programs_repository)
recommendations_procedure = RecommendationsProcedure(recommendations_repository)

# Создание нового пользователя
NewUser = User.User(5, 21, 'Мужчина', 75, 185, 'Андрей', 'Набрать мышечную массу')
user_procedure.add_user(NewUser)

# Добавление нового оборудования
NewEquipment = Equipment.Equipment(5, 'Гриф', 'Спортивный снаряд 20кг для основных упражнений')
equipment_procedure.add_equipment(NewEquipment)

# Добавление упражнения
NewExercise = Exercise.Exercise(5, 'Жим лежа', 'Сгибание и разгибание рук со штангой со свободным весом', 12)
exercises_procedure.add_exercise(NewExercise)

# Добавление мышечной группы
NewMuscle = MuscleGroup.MuscleGroup(5, 'Широчайшие мышцы спины', 'Спина')
muscle_groups_procedure.add_muscle_group(NewMuscle)

# Добавление программы тренировок
NewTraning = TrainingProgram.TrainingProgram(5, 'Пятница', NewExercise)

# Добавление рекомендации
NewRecommendation = Recommendations.Recommendations(5, 'Набор мышечной массы', 'Лучшее время суток для тренировок с целью наращивания массы – вечер')

