

class TrainingDay:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, TrainingDay):
            return False
        return self.name == other.name
