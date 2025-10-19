from dataclasses import dataclass
from enums import Diagnosis, Style

@dataclass
class UserProfile:

    name: str
    diagnosis: list[Diagnosis]
    communication_style: list[Style]
    tigger_words: list[str]


