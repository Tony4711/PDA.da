from enums import Chatter, Diagnosis
import readchar


class PDA_Utility:

    def read_raw_input():
         raw_input = input(f"[{Chatter.USER.value}]: ")
         return raw_input
    
    def chop_input(raw_input):
        chopped_input = [i.strip() for i in raw_input.split(",") if i.strip()]
        return chopped_input

    def print_input(who: Chatter, txt: str):
        print(f"[{who}]: {txt}")

    def get_valid_diagnosis(diagnosis):
        for d in Diagnosis:
            if d.value == diagnosis:
                return d