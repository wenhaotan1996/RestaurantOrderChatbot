# RestaurantOrderChatbot  
   
## To run the chatbot:  
You would need to have [Rasa](https://rasa.com/docs/rasa/installation/) (2.8.13)  
Run the following commands in order:  
Train the chatbot: `rasa train`  
Start the actions server: `rasa run actions`  
On a seperate terminal run chatbot interface: `rasa shell`  
   
## Conversation Flows Gauranteed to Work for Testing  
Flow #1: complete the order with a combo (one burger, one medium drink, with fries)  
- Greet the chat bot: `->hi`
- Ask how to order: `->How do I order`
- Ask about the combos: `->What combos do you have`
- Order one of the three combo: `->I would like a combo three`  
- Ask about drinks options: `->What drinks do you have`
- Specify the drink for this offer with one of the drink options: `->I would like a diet coke`
- Ask the bot for the price of the current order: `->How much is my order`  
- Abort current order and start a new one to test the other flow: `->I would like to start a new order`  
![Flow #1](/img/flow1.png "Flow #1 demo")
    
     
Flow #2: complete the order with items directly  
- Greet the chat bot: `->hi`
- Ask about burgers: `->What burgers do you have`
- Order one of the three burgers: `->I would like a double double`
- Choose "no fires" options for the order: `->no fries`
- Ask about drinks options: `->What drinks do you have`
- Order one of the drinks: `->I would like a Coke`
- Select a size: `->Medium`
- Ask the bot for the price of the current order: `->How much is my order`
![Flow #2](/img/flow2.png "Flow #2 demo")
   
Other features (could be asked throughout any conversation flow):   
- Ask the bot to repeat what you have so far: `->Repeat my order`
- Chat about the weather: `->The weather today is wonderful`
- Compliment the bot: `->You are wonderful`  
![Flow #2](/img/chitchat.png "Chitchat demo")
