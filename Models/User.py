import hashlib
from dataclasses import dataclass, field
from typing import List, Optional

from Models.TrainingProgram import TrainingProgram
from Models.Recommendations import Recommendations

@dataclass
class User:
    id: int
    age: int
    gender: str
    weight: float
    height: float
    name: str
    purpose: str
    username: str
    _password: str  # Зашифрованный пароль
    training_programs: List[TrainingProgram] = field(default_factory=list)  # У пользователя могут быть программы тренировок
    recommendations: Optional[Recommendations] = None  # Пользователь может иметь рекомендации

    def __post_init__(self):
        self._password = self._encrypt_password(self._password)

    @staticmethod
    def _encrypt_password(password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_password(self, password: str) -> bool:
        return self._password == self._encrypt_password(password)

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.id == other.id and
                    self.age == other.age and
                    self.gender == other.gender and
                    self.weight == other.weight and
                    self.height == other.height and
                    self.name == other.name and
                    self.purpose == other.purpose and
                    self.username == other.username)
        return False
