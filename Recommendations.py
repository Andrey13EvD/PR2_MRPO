

class Recommendations:
    def __init__(self, purpose, recommendations):
        self.purpose = purpose
        self.recommendations = recommendations

    def __eq__(self, other):
        if not isinstance(other, Recommendations):
            return False
        return (self.purpose == other.purpose) and (self.recommendations == other.recommendations)
