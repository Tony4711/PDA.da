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
          
    def talk_loop(self):
            self.answers = {}
            for q in self.questions:
                PDA_Utility.print_input(Chatter.BOT.value, q)
                user_txt = self.get_input()
                self.answers[q] = user_txt
            
    def create_new_user(self):
        user_name = input(">> ")
        diagnosis = {}
        key = self.read_input()
        while key != ('\r', '\n'):
            for i in (range(len(Diagnosis))):
                diagnosis[i] = input()
        user = UserProfile(user_name) 
                           #[Diagnosis.ADHS, Diagnosis.ASS, Diagnosis.PDA], [Style.PANDA, Style.HONEST, Style.DIRECT])