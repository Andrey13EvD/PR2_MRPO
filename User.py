class User:
    def __init__(self, name, age, height, weight, purpose, gender):
        self.id = id
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.purpose = purpose
        self.gender = gender

    def get_info(self):
        return [self.id, self.name, self.age, self.height, self.weight, self.purpose, self.gender]
