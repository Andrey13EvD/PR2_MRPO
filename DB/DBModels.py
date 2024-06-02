from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Ассоциативная таблица для связи Exercise и MuscleGroup
exercise_muscle_group = Table('exercise_muscle_group', Base.metadata,
    Column('exercise_id', Integer, ForeignKey('exercises.id'), primary_key=True),
    Column('muscle_group_id', Integer, ForeignKey('muscle_groups.id'), primary_key=True)
)

class Equipment(Base):
    __tablename__ = 'equipments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    repetitions = Column(Integer, nullable=False)
    equipment_id = Column(Integer, ForeignKey('equipments.id'), nullable=True)

    equipment = relationship("Equipment", back_populates="exercises")
    muscle_groups = relationship("MuscleGroup", secondary=exercise_muscle_group, back_populates="exercises")

Equipment.exercises = relationship("Exercise", order_by=Exercise.id, back_populates="equipment")

class MuscleGroup(Base):
    __tablename__ = 'muscle_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)

    exercises = relationship("Exercise", secondary=exercise_muscle_group, back_populates="muscle_groups")

class Recommendations(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True)
    purpose = Column(String, nullable=False)
    recommendations = Column(Text, nullable=False)

class TrainingProgram(Base):
    __tablename__ = 'training_programs'

    id = Column(Integer, primary_key=True)
    week_day = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    exercises = relationship("Exercise", secondary='training_program_exercises', back_populates="training_programs")
    user = relationship("User", back_populates="training_programs")

training_program_exercises = Table('training_program_exercises', Base.metadata,
    Column('training_program_id', Integer, ForeignKey('training_programs.id'), primary_key=True),
    Column('exercise_id', Integer, ForeignKey('exercises.id'), primary_key=True)
)

Exercise.training_programs = relationship("TrainingProgram", secondary=training_program_exercises, back_populates="exercises")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    name = Column(String, nullable=False)
    purpose = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    _password = Column(String, nullable=False)
    recommendations_id = Column(Integer, ForeignKey('recommendations.id'), nullable=True)

    training_programs = relationship("TrainingProgram", order_by=TrainingProgram.id, back_populates="user")
    recommendations = relationship("Recommendations", back_populates="users")

Recommendations.users = relationship("User", order_by=User.id, back_populates="recommendations")

# Создание соединения с базой данных
engine = create_engine('sqlite:///training_diary.db')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()
