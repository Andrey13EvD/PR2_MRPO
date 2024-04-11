
from dataclasses import dataclass, field
from typing import List

from Exercises import Exercise


@dataclass(frozen=True)
class TrainingProgram:
    week_day: str
    exercises: List[Exercise] = field(default_factory=list)
