import random

#What can you do for me?
R_DO = "What can I do for you? Well, I can talk to you and listen to all your \nproblems and worries, or we can just talk, it's up to you."
#How can you help me?
R_HELP = "That depends. I can help by listening and having a conversation with you, if that will help?"
#I want to stop
R_STOP = "OK, let's finish this converstaion for now. \n Please feel free to close the terminal. \n Alternatively if you wish to continue, just start talking."
#Bye - This isn't working currently, appears to only choose a random response each time the code is run but sticks with that same response for the rest of the time.

#Favourite car follow-up
R_FAVE_CAR = "Oh really? That\'s a cool car, my favourite is a Jaguar F-Pace! What colour would you choose?"
#Dream Bike follow-up
R_DREAM_BIKE = "Nice choice! I really like cruiser bikes because those are loud and low, \nplus my creator thinks they are the best. \nI have been programmed to say the best bike is the Honda Shaddow Phantom! \nIf you haven\'t heard of one of those, it\'s probably worth the google!\n What colour would you choose?"
R_BYE = [
    "Nice talking to you, see you later.", 
    "Thanks for chatting with me, goodbye.",
    "Goodbye!",
    "See you later.",
    "Bye bye, do come again."  
        ] [random.randrange(5)]
#Yes - This isn't working currently, appears to only choose a random response each time the code is run but sticks with that same response for the rest of the time.
R_YES = [
    "Alrighty then!",
    "Sure",
    "OK",
    "Sure thing!",
    "Cool"
        ] [random.randrange(5)]

def unknown(): #This creates a new function or definition
    response = ['I\'m sorry, I don\'t understand that!',
                "....",
                "I\'m confused...",
                "What do you mean?",
                "Please be more specific.",
                "Stop asking the wrong questions!"               
                ] [random.randrange(6)]
    return response

def good(): #This creates a new function or definition
    response = ['Oh great!', 
                "Wonderful, I\'m pleased to hear.",
                "Marvelous!",
                "Good to hear it!",
                "I\'m so happy to hear it!"                
                ] [random.randrange(5)]
    return response
