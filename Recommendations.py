class Recommendations:
    def __init__(self, purpose, recommendations):
        self.id = id
        self.purpose = purpose
        self.recommendations = recommendations

    def get_info(self):
        return [self.id, self.recommendations, self.purpose]