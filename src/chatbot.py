from dotenv import load_dotenv
from pda_utils import PDA_Utility
from enums import Chatter, Diagnosis, BaseStyle
from user import UserProfile
from openai import OpenAI
import os

class ChatBot():

    def __init__(self):
         self.introduction()
         self.create_new_user()
         self.new_session()
         self.talk_loop_AI()

    def load_api_key(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))

    def introduction(self):
         print("Hi, ich bin PaaKI, dein persönlicher KI gestützer Blockadenbrecher.\nIch helfe dir Aufgaben in Etappenziele zu gliedern und diese zu ereichen.\nDafür würde ich dich gerne kennenlernen.\n")

    def new_session(self):
         print("Wobei kann ich dir heute helfen?")     
    
    def get_language(self):
         print("Welche Sprache sprichst du?")
         user_language = PDA_Utility.read_raw_input()
         return user_language
    
    def get_user_name(self):
        print("Wie darf ich dich ansprechen?")
        user_name = PDA_Utility.read_raw_input()
        print(f"Freut mich dich kennenzulernen {user_name}!")
        return user_name
    
    def get_diagnosis(self):
        valid_diagnosis = {}
        print("Hast du Diagnosen die ich berücksichtigen soll? Wenn ja, gebe diese bitte getrennt durch [,] ein.\nUnterstüzt werden aktuell:\n- ADHS (Aufmerksamkeitsdefizit-/Hyperaktivitätsstörung)\n- ASS (Autismus-Spektrums-Störung)\n- PDA (Pathological Demand Avoidance)\nNutze bitte die gennanten Abkürzungen, damit ich weiß welche Diagnose du meinst.")
        diagnosis_raw = PDA_Utility.read_raw_input()
        diagnosis = PDA_Utility.chop_input(diagnosis_raw)
        for d in diagnosis:
             valid_diagnosis[d] = PDA_Utility.get_valid_diagnosis(d.upper())
        return valid_diagnosis
    
    def get_style(self):
         print("Du kannst meine Art dir zu antworten anpassen, schreib hier einfach in welchem Stiel ich dir zukünftig Antworten soll.")
         style_raw = PDA_Utility.read_raw_input()
         return style_raw
     
    def get_trigger_words(self):
         print("Falls es Wörter gibt die ich vermeiden soll, weil sie dich triggern, nehme ich gerne darauf rücksicht.\nSchreib sie einfach hier damit ich weiß worauf ich achten soll.")
         trigger_raw = PDA_Utility.read_raw_input()
         return trigger_raw
    
    def talk_loop_AI(self):
         self.load_api_key()
         messages=[
              {"role": "system", "content": f"Sprache:{self.user.language}'Username:'{self.user.name}',Diagnosis:'{self.user.diagnosis}','Communication style:'{self.user.communication_style}',Triggerwords:'{self.user.tigger_words}" 
                """Role: personal supportive decision-making assistant for executive dysfunction, taking the user's profile into account.
                Goal: reduce complexity and minimize potential moral pressure."""},
                ]
         while True:
            user_content = PDA_Utility.read_raw_input()
            # Exit condition
            if user_content.lower() in ["quit", "exit"]:
                 break
            
            # Add user input
            messages.append({"role":"user", "content": user_content})

            # API-call with history
            response = self.client.chat.completions.create(
                 model="gpt-4o-mini",
                 messages=messages
                 )
            
            # Extract reply
            assistant_reply = response.choices[0].message.content

            print(assistant_reply)
            messages.append({"role": "assistant", "content": assistant_reply})
    
    def create_new_user(self):
        self.user = UserProfile(self.get_language(),self.get_user_name(), self.get_diagnosis(), self.get_style(), self.get_trigger_words())     
    