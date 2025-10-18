from enums import Chatter
import readchar


class PDA_Utility:

    def get_input(self):
        user_input = input(f"[{Chatter.USER.value}]: ")
        return user_input

    def print_input(self, who: Chatter, txt: str):
        print(f"[{who}]: {txt}")
    
    def read_input(self):
        from readchar import readkey, key
        input = readkey().lower().strip()
        return input