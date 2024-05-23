from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, insert
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base
import xml.etree.ElementTree as ET
from DBModels import User, TrainingProgram, TrainingDay, Exercise, MuscleGroup, ExerciseInstance
from DBRepository import UserRepository, TrainingProgramRepository, TrainingDayRepository, ExerciseRepository, MuscleGroupRepository, ExerciseInstanceRepository

# Создаем движок и сессию
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Создаем базовую модель
Base = declarative_base()

# Определение моделей
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    weight = Column(Integer)
    height = Column(Integer)
    goal = Column(String)
    training_programs = relationship("TrainingProgram", back_populates="user")

class TrainingProgram(Base):
    __tablename__ = 'training_programs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="training_programs")
    training_days = relationship("TrainingDay", back_populates="training_program")

class TrainingDay(Base):
    __tablename__ = 'training_days'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    day_of_week = Column(String)
    training_program_id = Column(Integer, ForeignKey('training_programs.id'))
    training_program = relationship("TrainingProgram", back_populates="training_days")
    exercise_instances = relationship("ExerciseInstance", secondary='training_day_exercise_instance', back_populates="training_days")

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    repetitions = Column(Integer)
    muscle_groups = relationship("MuscleGroup", back_populates="exercises")

class MuscleGroup(Base):
    __tablename__ = 'muscle_groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    exercises = relationship("Exercise", back_populates="muscle_groups")

class ExerciseInstance(Base):
    __tablename__ = 'exercise_instances'
    id = Column(Integer, primary_key=True)
    training_day_id = Column(Integer, ForeignKey('training_days.id'))
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    training_days = relationship("TrainingDay", back_populates="exercise_instances")

# Ассоциативная таблица для связи TrainingDay и ExerciseInstance
training_day_exercise_instance = Table('training_day_exercise_instance', Base.metadata,
    Column('training_day_id', Integer, ForeignKey('training_days.id'), primary_key=True),
    Column('exercise_instance_id', Integer, ForeignKey('exercise_instances.id'), primary_key=True)
)

Base.metadata.create_all(engine)

# Инициализация репозиториев
user_repository = UserRepository(session)
training_program_repository = TrainingProgramRepository(session)
training_day_repository = TrainingDayRepository(session)
exercise_repository = ExerciseRepository(session)
muscle_group_repository = MuscleGroupRepository(session)
exercise_instance_repository = ExerciseInstanceRepository(session)

# Функции чтения данных из XML
def read_users_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    users = []
    for user_elem in root.findall('.//user'):
        user_data = {
            'id': int(user_elem.find('id').text),
            'name': user_elem.find('name').text,
            'age': int(user_elem.find('age').text),
            'gender': user_elem.find('gender').text,
            'weight': float(user_elem.find('weight').text),
            'height': float(user_elem.find('height').text),
            'goal': user_elem.find('purpose').text
        }
        users.append(user_data)
    return users

def read_training_programs_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    programs = []
    for program_elem in root.findall('.//training_program'):
        program_data = {
            'id': int(program_elem.find('id').text),
            'name': program_elem.find('name').text,
            'user_id': int(program_elem.find('user_id').text)
        }
        programs.append(program_data)
    return programs

def read_training_days_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    days = []
    for day_elem in root.findall('.//training_day'):
        day_data = {
            'id': int(day_elem.find('id').text),
            'name': day_elem.find('name').text,
            'day_of_week': day_elem.find('day_of_week').text,
            'training_program_id': int(day_elem.find('training_program_id').text)
        }
        days.append(day_data)
    return days

def read_exercises_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    exercises = []
    for exercise_elem in root.findall('.//exercise'):
        exercise_data = {
            'id': int(exercise_elem.find('id').text),
            'name': exercise_elem.find('name').text,
            'description': exercise_elem.find('description').text,
            'repetitions': int(exercise_elem.find('repetitions').text)
        }
        exercises.append(exercise_data)
    return exercises

def read_muscle_groups_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    muscle_groups = []
    for muscle_group_elem in root.findall('.//muscle_group'):
        muscle_group_data = {
            'id': int(muscle_group_elem.find('id').text),
            'name': muscle_group_elem.find('name').text
        }
        muscle_groups.append(muscle_group_data)
    return muscle_groups

def read_exercise_instances_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    exercise_instances = []
    for exercise_instance_elem in root.findall('.//exercise_instance'):
        exercise_instance_data = {
            'id': int(exercise_instance_elem.find('id').text),
            'training_day_id': int(exercise_instance_elem.find('training_day_id').text),
            'exercise_id': int(exercise_instance_elem.find('exercise_id').text)
        }
        exercise_instances.append(exercise_instance_data)
    return exercise_instances

if __name__ == "__main__":
    # Чтение данных из XML файлов
    users_data = read_users_from_xml('../data/users.xml')
    training_programs_data = read_training_programs_from_xml('../data/training_programs.xml')
    training_days_data = read_training_days_from_xml('../data/training_days.xml')
    exercises_data = read_exercises_from_xml('../data/exercises.xml')
    muscle_groups_data = read_muscle_groups_from_xml('../data/muscle_groups.xml')
    exercise_instances_data = read_exercise_instances_from_xml('../data/exercise_instances.xml')

    # Очистка данных в таблицах
    session.query(User).delete()
    session.query(TrainingProgram).delete()
    session.query(TrainingDay).delete()
    session.query(Exercise).delete()
    session.query(MuscleGroup).delete()
    session.query(ExerciseInstance).delete()

    # Запись пользователей в базу данных
    for user_data in users_data:
        user_repository.add(User(**user_data))

    # Запись программ тренировок в базу данных
    for program_data in training_programs_data:
        training_program_repository.add(TrainingProgram(**program_data))



    # Запись упражнений в базу данных
    for exercise_data in exercises_data:
        exercise_repository.add(Exercise(**exercise_data))

    # Запись групп мышц в базу данных
    for muscle_group_data in muscle_groups_data:
        muscle_group_repository.add(MuscleGroup(**muscle_group_data))

# Запись экземпляров упражнений в базу данных
    for exercise_instance_data in exercise_instances_data:
        exercise_instance_repository.add(ExerciseInstance(**exercise_instance_data))

    session.commit()


# Запись тренировочных дней в базу данных
    for day_data in training_days_data:
        training_day_repository.add(TrainingDay(**day_data))

