from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher

class ActionSetItemFromCombo(Action):
   def name(self) -> Text:
      return "action_set_item_from_combo"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      combo = tracker.get_slot('combo')
      burger = None
      if combo == "one":
         burger = "Double Double"
      elif combo == "two":
         burger = "Cheeseburger"
      elif combo == "three":
         burger = "Hamburger"
      if burger == None:
         return []
      else:
         return [SlotSet("burger",burger), SlotSet("fries", "fries"), SlotSet("size", "medium")]

class ActionResetAllSlots(Action):
   def name(self) -> Text:
      return "action_reset_all_slots"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      return [AllSlotsReset()]

class ActionComputePrice(Action):
   def name(self) -> Text:
      return "action_compute_price"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      prices = {
         "Double Double": 4.04,
         "Cheeseburger": 2.81,
         "Hamburger": 2.46,
         "fries": 1.87,
         "small": 1.75,
         "medium": 1.93,
         "large": 2.16
      }
      price = 0
      burger = tracker.get_slot('burger')
      drink = tracker.get_slot('drink')
      size = tracker.get_slot('size')
      fries = tracker.get_slot('fries')
      if burger != None and burger != "no burger":
         price += prices[burger]
      if burger != None and fries != "no fries":
         price += prices["fries"]
      if drink != None and size != None and drink != "no drink":
         price += prices[size]
      dispatcher.utter_message(text = ("Your current total charge of the order is going to be $" + str(price)))
      return []

class ValidateOrderForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_order_form"

    async def validate_drink(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

      combo = tracker.get_slot("combo")
      if value == "no drink" and combo == None:
         return {"drink": value, "size": "small"}
      elif value == "no drink" and combo != None:
         dispatcher.utter_message("A combo comes with a medium size drink. You could select one of the drinks or start a new order with items instead of combo")
         return {"drink": None}
      else:
         return {"drink": value}

class ActionRepeatOrder(Action):
   def name(self) -> Text:
      return "action_repeat_order"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      response = ""
      combo = tracker.get_slot('combo')
      burger = tracker.get_slot('burger')
      fries = tracker.get_slot('fries')
      drink = tracker.get_slot('drink')
      size = tracker.get_slot('size')
      if combo == None and burger == None:
         response = "You haven't order anything"     
      else:
         response = "At the moment, you have ordered"
         if combo != None:
            response += " combo " + combo + " with"
         if burger != None:
            response += " a " + burger
         if fries != None:
            response += ", " + fries
         if drink == "no drink":
            response += ", no drink"
         elif drink != None:
            response += ", " + drink
            if size != None:
               response += " of size " + size

      dispatcher.utter_message(text = response)
      return []