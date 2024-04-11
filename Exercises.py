

from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Exercise:
    name: str
    description: str
    required_equipment: List[str] = field(default_factory=list)
