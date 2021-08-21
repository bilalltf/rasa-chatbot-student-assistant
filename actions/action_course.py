from logging import NullHandler
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from sqlite3 import *
class ActionCourse(Action):
    def name(self) -> Text:
        return "action_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        exist = False
        l = ''
        subj = tracker.get_slot('subject')
        sect = tracker.get_slot('sector')
        c = connect("database.sqlite")
        cur = c.cursor()
        req = "select * from course"
        res = cur.execute(req)
        for ligne in res.fetchall():
            if (subj.lower() == ligne[1].lower() or subj.lower() == ligne[2].lower()) and (sect.lower() == ligne[3].lower() or sect.lower() == ligne[4].lower()):
               exist = True 
               l = ligne[6]
        c.close()
        response = """Vous pouvez télécharger le cours à partir ce lien {}""".format(l)

        if exist:
            dispatcher.utter_message(response)
        else: 
            dispatcher.utter_message(text = "Aucun cours ne correspondant à ces coordonnées")
        return [SlotSet('subject',NullHandler), SlotSet('sector',NullHandler)]
