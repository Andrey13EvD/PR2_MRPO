import datetime
from faker import Faker
from Models.User import User
from Models.Exercise import Exercise
from UoW.UnitOfWork import SqlAlchemyUnitOfWork
from Repository.UserRepository import UserRepository
from Repository.ExercisesRepository import ExercisesRepository
from DB.DBModels import User as UserModel
from DB.DBModels import Exercise as ExerciseModel

fake = Faker()

uow = SqlAlchemyUnitOfWork()

with uow:
    # Создание нескольких пользователей
    users = []
    for _ in range(5):
        user = UserModel(
            name=fake.name(),
            age=fake.random_int(min=18, max=60),
            gender=fake.random_element(elements=('male', 'female')),
            weight=fake.random_float(min=50, max=120),
            height=fake.random_float(min=150, max=200),
            purpose=fake.sentence(),
            username=fake.user_name(),
            password=fake.password(length=10)
        )
        users.append(user)
        uow.repository.add(user)

    # Создание нескольких упражнений для каждого пользователя
    for user in users:
        for _ in range(3):
            exercise = ExerciseModel(
                name=fake.word(),
                description=fake.sentence(),
                repetitions=fake.random_int(min=5, max=20),
                user_id=user.id,
                date=datetime.datetime.now() + datetime.timedelta(days=fake.random_int(min=1, max=30))
            )
            uow.repository.add(exercise)

    # Получение всех пользователей
    users_from_db = uow.repository.get_all(UserModel)
    for user in users_from_db:
        print(user)
