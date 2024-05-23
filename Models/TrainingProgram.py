from dataclasses import dataclass, field
from typing import List, Optional
from .Exercise import Exercise

@dataclass(frozen=True)
class TrainingProgram:
    id: int
    week_day: str
    exercises: Optional[List['Exercise']] = field(default_factory=list)
