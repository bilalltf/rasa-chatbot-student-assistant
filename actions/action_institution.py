from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from sqlite3 import *
class ActionCourse(Action):
    def name(self) -> Text:
        return "action_inst"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        exist = False
        l = ''
        inst = tracker.get_slot('inst_type')
        c = connect("database.sqlite")
        cur = c.cursor()

        if inst.lower() == 'faculté':
            req = "select * from institution where type = 'faculté'"
            l = "facultés"
        elif inst.lower() == 'école':
            req = "select * from institution where type = 'école'"
            l = "écoles"
        else:
            req = "select * from institution"
            l = "établissements"
        response = """Voilà les {} de l'université \n """.format(l)
        

        
        res = cur.execute(req)

        for ligne in res.fetchall():
            response += """- {}, lien {} \n""".format(ligne[1], ligne[3])
            
        dispatcher.utter_message(response)

            
        c.close()
        

    
        return [SlotSet('inst_type', None)]
