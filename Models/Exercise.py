from dataclasses import dataclass, field
from typing import List, Optional

from Models import Equipment


@dataclass(frozen=True)
class Exercise:
    id: int
    name: str
    description: str
    repetitions: int
    equipment: Optional[Equipment] = None  # Упражнение может использовать оборудование
    muscle_groups: List['MuscleGroup'] = field(default_factory=list)  # Упражнение нацелено на группы мышц