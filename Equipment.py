from dataclasses import dataclass

@dataclass(frozen=True)
class Equipment:
    name: str
    description: str
