from dataclasses import dataclass
from enums import Diagnosis, BaseStyle

@dataclass
class UserProfile:

    name: str
    language: str
    diagnosis: list[Diagnosis]
    communication_style: list[BaseStyle]
    tigger_words: list[str]


