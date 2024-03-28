from tabulate import tabulate
from Exercises import Exercise
from Equipment import Equipment
from User import User
from TrainingProgram import TrainingProgram

def main():

    exercise1 = Exercise("Приседания", "Упражнение для нижних конечностей")
    exercise2 = Exercise("Жим гантелей лежа", "Упражнение для груди")
    equipment1 = Equipment("Гантели", "Ручные грузы")
    equipment2 = Equipment("Брусья", "Оборудование для отжиманий")
    user1 = User("John", 30, 1.75, 75, "Сбросить вес", "Мужчина")


    exercises_data = [
        [exercise1.name, exercise1.description],
        [exercise2.name, exercise2.description]
    ]
    equipment_data = [
        [equipment1.name, equipment1.description],
        [equipment2.name, equipment2.description]
    ]
    users_data = [
        [user1.name, user1.age, user1.height, user1.weight, user1.purpose, user1.gender]
    ]

    print("Упражнения:")
    print(tabulate(exercises_data, headers=["Название", "Описание"], tablefmt="grid"))
    print("\nОборудование:")
    print(tabulate(equipment_data, headers=["Название", "Описание"], tablefmt="grid"))
    print("\nПользователи:")
    print(tabulate(users_data, headers=["Имя", "Возраст", "Рост", "Вес", "Цель", "Пол"], tablefmt="grid"))

if __name__ == "__main__":
    main()
