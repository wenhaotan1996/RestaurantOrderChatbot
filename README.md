# RestaurantOrderChatbot  
   
## To run the chatbot:  
You would need to have [Rasa](https://rasa.com/docs/rasa/installation/) and python [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) installed  
Run the following commands in order:  
Train the model: `rasa train`  
Start the actions server: `rasa run actions`  
On a seperate terminal run chatbot interface: `rasa shell`  
   
## Conversation Flows Gauranteed to Work for Testing  
Flow #1: complete the order with a combo (one burger, one medium drink, with fries)  
- Greet the chat bot: `->hi`
- Ask about the combos: `->What combos do you have`
- Order one of the three combo: `->combo three`  
- Specify the drink for this offer with one of the drink options: `->diet coke`
- Ask the bot for the price of the current order: `->get price`  
    
     
Flow #2: complete the order with items directly  
- Greet the chat bot: `->hi`
- Ask about burgers: `->What burgers do you have`
- Order one of the three burgers: `->double double`
- Choose "no fires" options for the order: `->no fries`
- Ask about drinks options: `->What drinks do you have`
- Order one of the drinks: `->Coke`
- Select a size: `->Medium`
- Ask the bot for the price of the current order: `->get price`
