from dataclasses import dataclass, field
from typing import List, Optional

@dataclass(frozen=True)
class User:
    id: int
    age: int
    gender: str
    weight: float
    height: float
    name: str
    purpose: str

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.id == other.id and
                    self.age == other.age and
                    self.gender == other.gender and
                    self.weight == other.weight and
                    self.height == other.height and
                    self.name == other.name and
                    self.purpose == other.purpose)
        return False
