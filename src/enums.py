from enum import Enum, auto

class Chatter(Enum):

    BOT = "Bot"
    USER = "User"

class Diagnosis(Enum):

    PDA = "PDA"
    ADHS = "ADHS"
    ASS = "ASS"

class BaseStyle(Enum):

    CALM = "ruhig"
    PANDA = "Kämpfe weise auswählen, Angstmanagement, Verhandlung & Zusammenarbeit, Anforderungen verschleiern & managen, Anpassung"
    DIRECT = "direkt"
    EMPATHIC = "emphatisch"
    HONEST = "ehrlich"

