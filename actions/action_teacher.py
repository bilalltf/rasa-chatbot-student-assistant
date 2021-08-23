from logging import NullHandler
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from sqlite3 import *
class ActionCourse(Action):
    def name(self) -> Text:
        return "action_teacher"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        exist = False
        teacher = ''
        subj = tracker.get_slot('subject')
        sect = tracker.get_slot('sector')
        c = connect("database.sqlite")
        cur = c.cursor()
        req = "select * from course"
        res = cur.execute(req)
        for ligne in res.fetchall():
            if (subj.lower() == ligne[1].lower() or subj.lower() == ligne[2].lower()) and (sect.lower() == ligne[3].lower() or sect.lower() == ligne[4].lower()) and ligne[5] != None and ligne[5] != '':
               exist = True 
               teacher = ligne[5]
        c.close()
        

        if exist:
            response = """Le professeur du module {} filière {} est {}""".format(subj, sect, teacher)
            dispatcher.utter_message(response)
        else: 
            dispatcher.utter_message(text = "Aucun professeur ne correspondant à ces coordonnées")
        return [SlotSet('subject',NullHandler), SlotSet('sector',NullHandler)]
