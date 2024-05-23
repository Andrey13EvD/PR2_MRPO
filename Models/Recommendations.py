from dataclasses import dataclass, field


@dataclass(frozen=True)
class Recommendations:
    id: int
    purpose: str
    recommendations: str
