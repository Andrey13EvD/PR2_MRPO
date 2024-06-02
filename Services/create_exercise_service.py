from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from DB.DBModels import Exercise, Equipment, MuscleGroup, engine

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

def create_exercise(name: str, description: str, repetitions: int, equipment_id: int = None, muscle_group_ids: list = None) -> Exercise:
    try:
        # Найти оборудование по ID (если указано)
        equipment = None
        if equipment_id:
            equipment = session.query(Equipment).filter_by(id=equipment_id).first()
            if not equipment:
                print(f"Ошибка: Оборудование с ID {equipment_id} не существует.")
                return None

        # Найти группы мышц по ID (если указаны)
        muscle_groups = []
        if muscle_group_ids:
            muscle_groups = session.query(MuscleGroup).filter(MuscleGroup.id.in_(muscle_group_ids)).all()
            if not muscle_groups:
                print(f"Ошибка: Один или несколько групп мышц IDs {muscle_group_ids} не существуют.")
                return None

        # Создать новое упражнение
        new_exercise = Exercise(
            name=name,
            description=description,
            repetitions=repetitions,
            equipment=equipment,
            muscle_groups=muscle_groups
        )

        # Добавить упражнение в сессию и сохранить изменения в базе данных
        session.add(new_exercise)
        session.commit()
        print("Упражнение успещно добавлено!")
        return new_exercise
    except IntegrityError:
        session.rollback()
        print("Ошибка: Произошла ошибка целостности.")
        return None
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
        return None

# Пример использования
if __name__ == "__main__":
    # Пример данных для нового упражнения
    name = "Отжимания"
    description = "Базовое упражнение для верхней части тела."
    repetitions = 15
    equipment_id = None  # Например, это упражнение не требует оборудования
    muscle_group_ids = [1, 2]  # Предположим, что ID 1 и 2 существуют в MuscleGroup

    created_exercise = create_exercise(name, description, repetitions, equipment_id, muscle_group_ids)

    if created_exercise:
        print(f"Упражнение {created_exercise.name} создано с ID: {created_exercise.id}")
    else:
        print("Не удалось создать упражнение.")
