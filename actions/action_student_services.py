from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from sqlite3 import *



class student_details_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_student_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ['type_service', 'sector']
        if tracker.slots.get('type_service') == 'cours' or tracker.slots.get('type_service') == 'prof':
            required_slots +=['subject']
        elif tracker.slots.get('type_service') == 'emploi':
            required_slots +=['semester']

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]


        # All slots are filled.
        return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_student_services"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        exist = False
        
        sect = tracker.get_slot('sector')
        ts = tracker.get_slot('type_service')

        #connect to database & and select data

        c = connect("database.sqlite")
        cur = c.cursor()
        req = "select * from course"
        res = cur.execute(req)

        

        if ts == "cours":
            subj = tracker.get_slot('subject')
            l = ''
            for ligne in res.fetchall():
                if (subj.lower() == ligne[1].lower() or subj.lower() == ligne[2].lower()) and (sect.lower() == ligne[3].lower() or sect.lower() == ligne[4].lower()):
                    exist = True 
                    l = ligne[6]
            c.close()
            response = """Vous pouvez télécharger le cours de {} filière {} à partir ce lien :\n {}""".format(subj, sect, l)

            if exist:
                dispatcher.utter_message(response)
            else: 
                dispatcher.utter_message(text = "Aucun cours ne correspondant à ces coordonnées")
            return [SlotSet('subject', None), SlotSet('sector',None)]
        elif ts == 'prof':
            subj = tracker.get_slot('subject')

            for ligne in res.fetchall():
                if (subj.lower() == ligne[1].lower() or subj.lower() == ligne[2].lower()) and (sect.lower() == ligne[3].lower() or sect.lower() == ligne[4].lower()) and ligne[5] != '':
                    exist = True 
                    teacher = ligne[5]
            c.close()
        

            if exist:
                response = """Le professeur du module {} filière {} est {}""".format(subj, sect, teacher)
                dispatcher.utter_message(response)
            else: 
                dispatcher.utter_message(text = "Aucun professeur ne correspondant à ces coordonnées")
            return [SlotSet('subject', None), SlotSet('sector', None)]

        elif ts== 'emploi':
            s = tracker.get_slot('semester')
            req = "SELECT link from time_planning where lower(sector) = '" + sect.lower() + "' AND lower(semester) = '" + s.lower() + "'"
            res = cur.execute(req)
            link = res.fetchone()[0]
            if link != "" and link is not None:
                exist = True
                response="""Emploi de temps: filière {} semistre {} :\n {}""".format(sect, s, link)
                dispatcher.utter_message(response)
            if exist is False: 
                dispatcher.utter_message(text="Aucun emploi ne correspondant à ces coordonnées où bien il n'est pas encore disponible :(")


