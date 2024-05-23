from dataclasses import dataclass

@dataclass(frozen=True)
class Equipment:
    id: int
    name: str
    description: str
