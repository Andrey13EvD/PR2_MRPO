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


class TrainingProgram(Base):
    __tablename__ = 'training_programs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    week_day = Column(String)
    goal = Column(String)
    recommendation = Column(String)


class TrainingDay(Base):
    __tablename__ = 'training_days'

    id = Column(Integer, primary_key=True)
    training_program_id = Column(Integer, ForeignKey('training_programs.id'))
    day_of_week = Column(String)



class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    image_video = Column(String)
    equipment = Column(String)
    muscle_group_id = Column(Integer, ForeignKey('muscle_groups.id'))



class MuscleGroup(Base):
    __tablename__ = 'muscle_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)



class ExerciseInstance(Base):
    __tablename__ = 'exercise_instances'

    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    training_day_id = Column(Integer, ForeignKey('training_days.id'))
    repetitions = Column(Integer)

