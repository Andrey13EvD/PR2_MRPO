from sqlalchemy.orm import sessionmaker
from DB.DBModels import Equipment, MuscleGroup, Exercise, Recommendations, TrainingProgram, User, engine
import hashlib

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()


def encrypt_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def fill_db():
    # Добавление оборудования
    equipment_list = [
        Equipment(name="Гантели", description="Снаряд для силовых тренировок"),
        Equipment(name="Турник", description="Оборудование для подтягиваний"),
        Equipment(name="Беговая дорожка", description="Оборудование для кардиотренировок")
    ]
    session.add_all(equipment_list)

    # Добавление групп мышц
    muscle_group_list = [
        MuscleGroup(name="Грудные мышцы", category="Верхняя часть тела"),
        MuscleGroup(name="Бицепсы", category="Верхняя часть тела"),
        MuscleGroup(name="Трицепсы", category="Верхняя часть тела"),
        MuscleGroup(name="Пресс", category="Корпус"),
        MuscleGroup(name="Квадрицепсы", category="Нижняя часть тела")
    ]
    session.add_all(muscle_group_list)

    # Сохранение изменений для получения ID добавленных объектов
    session.commit()

    # Добавление упражнений
    exercise_list = [
        Exercise(
            name="Отжимания",
            description="Упражнение для тренировки грудных мышц и трицепсов",
            repetitions=15,
            muscle_groups=[muscle_group_list[0], muscle_group_list[2]]  # Грудные мышцы и трицепсы
        ),
        Exercise(
            name="Подтягивания",
            description="Упражнение для тренировки бицепсов и спины",
            repetitions=10,
            equipment=equipment_list[1],  # Турник
            muscle_groups=[muscle_group_list[1]]  # Бицепсы
        ),
        Exercise(
            name="Приседания",
            description="Упражнение для тренировки квадрицепсов",
            repetitions=20,
            muscle_groups=[muscle_group_list[4]]  # Квадрицепсы
        )
    ]
    session.add_all(exercise_list)

    # Добавление рекомендаций
    recommendation_list = [
        Recommendations(
            purpose="Похудение",
            recommendations="Снижение калорийности питания, увеличение кардио тренировок"
        ),
        Recommendations(
            purpose="Набор массы",
            recommendations="Увеличение калорийности питания, силовые тренировки"
        )
    ]
    session.add_all(recommendation_list)

    # Сохранение изменений для получения ID добавленных объектов
    session.commit()

    # Добавление пользователей
    user_list = [
        User(
            age=30,
            gender="мужской",
            weight=80.0,
            height=180.0,
            name="Иван Иванов",
            purpose="Похудение",
            username="ivan",
            _password=encrypt_password("ivan123"),
            recommendations_id=recommendation_list[0].id
        ),
        User(
            age=25,
            gender="женский",
            weight=60.0,
            height=165.0,
            name="Анна Смирнова",
            purpose="Набор массы",
            username="anna",
            _password=encrypt_password("anna123"),
            recommendations_id=recommendation_list[1].id
        )
    ]
    session.add_all(user_list)

    # Сохранение изменений для получения ID добавленных объектов
    session.commit()

    # Добавление программ тренировок для пользователей
    training_program_list = [
        TrainingProgram(
            week_day="Понедельник",
            user_id=user_list[0].id,
            exercises=[exercise_list[0], exercise_list[1]]  # Отжимания и подтягивания
        ),
        TrainingProgram(
            week_day="Среда",
            user_id=user_list[0].id,
            exercises=[exercise_list[2]]  # Приседания
        ),
        TrainingProgram(
            week_day="Вторник",
            user_id=user_list[1].id,
            exercises=[exercise_list[0], exercise_list[2]]  # Отжимания и приседания
        )
    ]
    session.add_all(training_program_list)

    # Сохранение изменений
    session.commit()

    print("Database filled successfully!")


if __name__ == "__main__":
    fill_db()
