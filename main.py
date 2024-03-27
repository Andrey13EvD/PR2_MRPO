import Equipment, Exercises, MuscleGroup, Recommendations, TrainingDay, TrainingProgram, User

from Repository import UserRepository as ur

user1 = User.User("Андрей", 20, 184, 73, "Набрать мышечную массу", "Мужской")
user2 = User.User("Тилек", 21, 178, 82, "Сбросить лишний вес", "Мужской")

equipment1 = Equipment.Equipment("Беговая дорожка", "Для бега")

exercise1 = Exercises.Exercises("Подтягивание", "Сгибание и разгибание рук на перекладине")

muscle1 = MuscleGroup.MuscleGroup("Предплечье", "Руки")

recommendation1 = Recommendations.Recommendations("Сбросить лишний вес", "Работа с меньшим весом на много повторений")

trainingDay1 = TrainingDay.TrainingDay("Силовая")

trainingProgram1 = TrainingProgram.TrainingProgram("Понедельник")

uRep = ur.UserRepository()

uRep.add(user1)
uRep.add(user2)

print(uRep.get_all())

uRep.remove(user2)
print(uRep.get_by_name("Андрей"))
print(uRep.get_by_name("73"))

print(exercise1.get_info())
print(muscle1.get_info())