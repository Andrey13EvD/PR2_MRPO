class MuscleGroup:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __eq__(self, other):
        if not isinstance(other, MuscleGroup):
            return False
        return (self.name == other.name) and (self.category == other.category)
