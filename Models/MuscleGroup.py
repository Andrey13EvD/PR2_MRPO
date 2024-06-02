class MuscleGroup:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def get_info(self):
        return [self.name, self.category]

    def __eq__(self, other):
        if isinstance(other, MuscleGroup):
            return (self.id, self.name, self.category) == (other.id, other.name, other.category)
        return False