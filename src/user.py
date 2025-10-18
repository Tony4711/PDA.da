from enums import Diagnosis, Style


class UserProfile:

    name: str
    diagnosis: list[Diagnosis]
    communication_sytel: list[Style]
    tigger_words: list[str]


