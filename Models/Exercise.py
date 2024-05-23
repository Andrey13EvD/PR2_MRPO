from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen=True)
class Exercise:
    id: int
    name: str
    description: str
    repetitions: int
