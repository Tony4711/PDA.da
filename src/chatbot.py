from dotenv import load_dotenv
from pda_utils import PDA_Utility
from enums import Chatter, Diagnosis, Style
from user import UserProfile
from openai import OpenAI
import os

class ChatBot():

    def load_api_key(self):
        load_dotenv()
        client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))

    def get_user_name(self):
        user_name = PDA_Utility.read_raw_input()
        return user_name
    
    def get_diagnosis(self):
        valid_diagnosis = {}
        diagnosis_raw = PDA_Utility.read_raw_input()
        diagnosis = PDA_Utility.chop_input(diagnosis_raw)
        for d in diagnosis:
             valid_diagnosis[d] = PDA_Utility.get_valid_diagnosis(d)
        return valid_diagnosis
    
    def get_style(self):
         pass
    
    def get_trigger_words(self):
         pass

    def talk_loop(self):
            self.answers = {}
            for q in self.questions:
                PDA_Utility.print_input(Chatter.BOT.value, q)
                user_txt = self.get_input()
                self.answers[q] = user_txt    
    
    def create_new_user(self):
        user = UserProfile(self.get_user_name(), self.get_diagnosis(), self.get_style(), self.get_trigger_words())     
        print(user)
    