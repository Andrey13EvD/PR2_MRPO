from Repository import FakeRepository

class TrainingProgramRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self._training_programs = []

    def add(self, training_program):
        self._training_programs.append(training_program)

    def remove(self, training_program):
        if self._training_programs:
            for tp in self._training_programs:
                if tp.id == training_program.id:
                    self._training_programs.remove(tp)

    def get_all(self):
        return self._training_programs

    def get_by_id(self, tp_id):
        for tp in self._training_programs:
            if tp.id == tp_id:
                return tp
        return None

    def get_by_week_day(self, week_day):
        for tp in self._training_programs:
            if tp.week_day == week_day:
                return tp
        return None
