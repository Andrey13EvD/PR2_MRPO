from sqlalchemy import Column, Integer, String, ForeignKey, Table, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    goal = Column(String)
    gender = Column(String)

    training_programs = relationship('TrainingProgram', back_populates='user')


class TrainingProgram(Base):
    __tablename__ = 'training_programs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    goal = Column(String)
    recommendation = Column(String)

    user = relationship('User', back_populates='training_programs')
    training_days = relationship('TrainingDay', back_populates='training_program')


class TrainingDay(Base):
    __tablename__ = 'training_days'

    id = Column(Integer, primary_key=True)
    training_program_id = Column(Integer, ForeignKey('training_programs.id'))
    day_of_week = Column(String)

    training_program = relationship('TrainingProgram', back_populates='training_days')
    exercises = relationship('Exercise', back_populates='training_day')


class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    image_video = Column(String)
    equipment = Column(String)
    muscle_group_id = Column(Integer, ForeignKey('muscle_groups.id'))

    muscle_group = relationship('MuscleGroup', back_populates='exercises')
    training_days = relationship('TrainingDay', secondary='exercise_training_day', back_populates='exercises')


class MuscleGroup(Base):
    __tablename__ = 'muscle_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)

    exercises = relationship('Exercise', back_populates='muscle_group')


exercise_training_day = Table('exercise_training_day', Base.metadata,
                              Column('exercise_id', Integer, ForeignKey('exercises.id')),
                              Column('training_day_id', Integer, ForeignKey('training_days.id'))
                              )


class ExerciseInstance(Base):
    __tablename__ = 'exercise_instances'

    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    training_day_id = Column(Integer, ForeignKey('training_days.id'))
    repetitions = Column(Integer)

    exercise = relationship('Exercise')
    training_day = relationship('TrainingDay')

# При необходимости, создаем двигатель и сессию:
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///:memory:')
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()
