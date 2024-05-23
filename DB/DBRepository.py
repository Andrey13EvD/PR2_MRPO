from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from DBModels import User, TrainingProgram, TrainingDay, Exercise, MuscleGroup, ExerciseInstance

class BaseRepository(ABC):
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

class UserRepository(BaseRepository):
    def add(self, user: User):
        try:
            self.session.add(user)
            self.session.commit()
        except IntegrityError:
            print("Пользователь уже есть в БД")
            self.session.rollback()

    def remove(self, user_id: int):
        user = self.session.query(User).filter_by(id=user_id).first()
        if user:
            try:
                self.session.delete(user)
                self.session.commit()
                print(f"Пользователь с ID {user_id} удален.")
            except IntegrityError:
                print("Ошибка удаления пользователя")
                self.session.rollback()
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def get_all(self):
        return self.session.query(User).all()

class TrainingProgramRepository(BaseRepository):
    def add(self, training_program: TrainingProgram):
        try:
            self.session.add(training_program)
            self.session.commit()
        except IntegrityError:
            print("Программа тренировок уже есть в БД")
            self.session.rollback()

    def remove(self, program_id: int):
        program = self.session.query(TrainingProgram).filter_by(id=program_id).first()
        if program:
            try:
                self.session.delete(program)
                self.session.commit()
                print(f"Программа тренировок с ID {program_id} удалена.")
            except IntegrityError:
                print("Ошибка удаления программы тренировок")
                self.session.rollback()
        else:
            print(f"Программа тренировок с ID {program_id} не найдена.")

    def get_all(self):
        return self.session.query(TrainingProgram).all()

class TrainingDayRepository(BaseRepository):
    def add(self, training_day: TrainingDay):
        try:
            self.session.add(training_day)
            self.session.commit()
        except IntegrityError:
            print("Тренировочный день уже есть в БД")
            self.session.rollback()

    def remove(self, day_id: int):
        day = self.session.query(TrainingDay).filter_by(id=day_id).first()
        if day:
            try:
                self.session.delete(day)
                self.session.commit()
                print(f"Тренировочный день с ID {day_id} удален.")
            except IntegrityError:
                print("Ошибка удаления тренировочного дня")
                self.session.rollback()
        else:
            print(f"Тренировочный день с ID {day_id} не найден.")

    def get_all(self):
        return self.session.query(TrainingDay).all()

class ExerciseRepository(BaseRepository):
    def add(self, exercise: Exercise):
        try:
            self.session.add(exercise)
            self.session.commit()
        except IntegrityError:
            print("Упражнение уже есть в БД")
            self.session.rollback()

    def remove(self, exercise_id: int):
        exercise = self.session.query(Exercise).filter_by(id=exercise_id).first()
        if exercise:
            try:
                self.session.delete(exercise)
                self.session.commit()
                print(f"Упражнение с ID {exercise_id} удалено.")
            except IntegrityError:
                print("Ошибка удаления упражнения")
                self.session.rollback()
        else:
            print(f"Упражнение с ID {exercise_id} не найдено.")

    def get_all(self):
        return self.session.query(Exercise).all()

class MuscleGroupRepository(BaseRepository):
    def add(self, muscle_group: MuscleGroup):
        try:
            self.session.add(muscle_group)
            self.session.commit()
        except IntegrityError:
            print("Группа мышц уже есть в БД")
            self.session.rollback()

    def remove(self, muscle_group_id: int):
        muscle_group = self.session.query(MuscleGroup).filter_by(id=muscle_group_id).first()
        if muscle_group:
            try:
                self.session.delete(muscle_group)
                self.session.commit()
                print(f"Группа мышц с ID {muscle_group_id} удалена.")
            except IntegrityError:
                print("Ошибка удаления группы мышц")
                self.session.rollback()
        else:
            print(f"Группа мышц с ID {muscle_group_id} не найдена.")

    def get_all(self):
        return self.session.query(MuscleGroup).all()

class ExerciseInstanceRepository(BaseRepository):
    def add(self, exercise_instance: ExerciseInstance):
        try:
            self.session.add(exercise_instance)
            self.session.commit()
        except IntegrityError:
            print("Инстанс упражнения уже есть в БД")
            self.session.rollback()

    def remove(self, exercise_instance_id: int):
        exercise_instance = self.session.query(ExerciseInstance).filter_by(id=exercise_instance_id).first()
        if exercise_instance:
            try:
                self.session.delete(exercise_instance)
                self.session.commit()
                print(f"Инстанс упражнения с ID {exercise_instance_id} удален.")
            except IntegrityError:
                print("Ошибка удаления инстанса упражнения")
                self.session.rollback()
        else:
            print(f"Инстанс упражнения с ID {exercise_instance_id} не найден.")

    def get_all(self):
        return self.session.query(ExerciseInstance).all()
