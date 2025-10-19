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
        print(">>> Bitte gebe deinen Benutzer Namen ein")
        user_name = PDA_Utility.read_raw_input()
        return user_name
    
    def get_diagnosis(self):
        valid_diagnosis = {}
        print(">>> Bitte gebe deine Diagnosen getrennt durch [,] ein")
        diagnosis_raw = PDA_Utility.read_raw_input()
        diagnosis = PDA_Utility.chop_input(diagnosis_raw)
        for d in diagnosis:
             valid_diagnosis[d] = PDA_Utility.get_valid_diagnosis(d)
        return valid_diagnosis
    
    def get_style(self):
         print(">>> Bitte gebe deinen bevorzugten Kommunikationsstil ein")
         style_raw = PDA_Utility.read_raw_input()
         return style_raw
     
    def get_trigger_words(self):
         print(">>> Bitte gebe Wörter ein die ich vermeiden soll")
         trigger_raw = PDA_Utility.read_raw_input()
         return trigger_raw
    
    def talk_loop_AI(self):
         client = OpenAI()
         response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"'Username:'{self.user.name}',Diagnosis:'{self.user.diagnosis}','Communicationstyle:'{self.user.communication_style}',Triggerwords:'{self.user.tigger_words}" },
                {"role": "user", "content": "User message or combined UserProfile data here..."}
    ]
)
    def talk_loop(self):
            self.answers = {}
            for q in self.questions:
                PDA_Utility.print_input(Chatter.BOT.value, q)
                user_txt = self.get_input()
                self.answers[q] = user_txt    
    
    def create_new_user(self):
        self.user = UserProfile(self.get_user_name(), self.get_diagnosis(), self.get_style(), self.get_trigger_words())     
        print(self.user)
    