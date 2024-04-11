from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int
    height: float
    weight: float
    purpose: str
    gender: str
