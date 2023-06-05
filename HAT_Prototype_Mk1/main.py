# Welcome to HAT (Helpful Artificial Talkbot)

import re #This means regular expression and helps to overcome the uppercase and lowercase issues.
import long_responses as long #This imports an additional file csalled long_responses



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):#def creates a new function or definition, followed by the parameters. Here this is saying that the function message_probability with have input from user_message, recognised_words, single_response (set to false by default) and required words.
    message_certainty = 0 #This means that there is not always going to be a message
    has_required_words = True #This means to only output IF has the required words

# Counts how many words are present in each predefined message
    for word in user_message: #this is saying for each word in the user message run below
        if word in recognised_words: #This if statement says that if the word is in the recognised words change message certainty to 1 or equal to 1.
            message_certainty += 1 #This changes the message_certainty that I predefined above to 1 from 0. 

# Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words)) # This is saying the percentage will equal the message certainty divided by the length of the recognised words

    # Checks that the required words are in the string
    for word in required_words: #This is saying for each word that is in the required words run below
        if word not in user_message: #This is an if statement that is saying if the word is not in the user_message then run below
            has_required_words = False #This changes the has_required_words to False from the predefined value of True from above.
            break #this breaks the code

    if has_required_words or single_response: #This is an if statement that is checking that if the response has either required words or single response then run the below
        return int(percentage*100) #This will turn the percentage into the nearest whole number
    else: #This is an else statement which means if the above parameters aren't met run this instead.
        return 0 #Means nothing matched

def check_all_messages(message): #This creates a new function or definition, followed by the parameters.
    highest_prob_list = {}


    def response(hat_response, list_of_words, single_response=False, required_words=[]): #This creates a new function or definition, followed by the parameters. This is saying that response will come from either hat_response, list_of_words, single_response, required_words and to run the below code.
        nonlocal highest_prob_list #Nonlocal is an override term, it allows for the highes probability list to be output
        highest_prob_list[hat_response] = message_probability(message, list_of_words, single_response, required_words) #This is essentially creating a variable 
        #'highest_prob_list[hat_response] which is populated by message_probability(message, list_of_words, single_response, required_words)

#------------------------------ RESPONSES START ------------------------------
    #Welcome
    response('Hello! Welcome to HAT, the chatbot designed for you. \n How are you doing?', ['hello', 'hi', 'hey', 'yo'], single_response=True)
    
    
    
    #----------------------------------- WELLBEING CHECK START ----------------------------------------
    
    #how are you?
    response('I\'m doing well, thank you. What about you, are you well?', ['how', 'are', 'you', 'doing',], required_words=['how', 'you'])
    
    #I'm good you?
    response('Glad to hear, I\'m  great now that I\'m speaking with you!', ['im', 'good', 'thanks', 'and', 'you'], required_words=['good', 'thanks', 'you'])
    
    #Not great
    response('Sorry to hear that, Perhaps talking with me will cheer you up!', ['im', 'not', 'so', 'good', 'down', 'sad', 'unwell' 'thanks', 'and', 'you'], required_words=['not', 'thanks', 'you'])
    
    #Upbeat
    response('That\'s swell to hear! I hope you stay feeling that way all day.', ['im', 'great', 'happy', 'upbeat', 'wonderful', 'swell', 'fabulous'], required_words=['im'])
    
    #Down/sad
    response('Oh no! That\'s not good. Hopefully by talking with me that\'ll lift your spirits a little.', ['sad', 'down', 'fed up', 'depressed', 'upset', 'frustrated'], required_words=['im'])
    
    #Neutral
    response('Cool. So, what would you like to talk about? \n - Science? \n - The Weather? \n - Cars? \n - Motorbikes? \n - Disney? \n - Colours? \n - Animals? \n - About Me?', ['fine', 'ok', 'so so', 'hanging in there'], required_words=['im'])
    
     #----------------------------------- WELLBEING CHECK END ----------------------------------------
    
    
    
    #Secret
    response('Nope! I can\'t keep a secret, my creator will only go and find out!', ['can', 'i', 'tell', 'you', 'a', 'secret'], required_words=['you', 'secret'])
    
    
    
    #----------------------------------- ABOUT ME START ----------------------------------------
    
    #About me
    response('Sure, what would you like to know?', ['about', 'you', 'tell', 'me'], required_words=['about'])
    
    #What is your name?
    response('My name is HAT', ['what', 'is', 'your', 'name'], required_words=['your', 'name'])
    
    #What does HAT stand for?
    response('HAT stands for Helpful Artificial Talkbot!', ['what', 'does', 'hat', 'stand', 'for'], required_words=['hat', 'stand', 'for'])
    
    #Who are you?
    response('I am HAT, here to talk to you whenever you want!', ['who', 'are', 'you'], required_words=['who', 'you'])
    
    #What do you want?
    response('I just want to be friends and make light conversation...', ['what', 'do', 'you', 'want',], required_words=['what', 'you', 'want'])
    
    #What do you do?
    response('I chat with people and make friends, I\'m nonjudgmental and won\'t shame you in any way. I just wish to be a nice friend to you!', ['what', 'do', 'you'], required_words=['what', 'you', 'do'])
    
    #Who made you?
    response('I was made by Charles Skudder, he created me as a prototype to see how I would get on. \n He plans lots of upgrades and changes to my coding all the time!', ['who', 'is', 'creator', 'created', 'you'], required_words=['who', 'created', 'you'])
    
    #----------------------------------- ABOUT ME END ----------------------------------------
    
    
    
    #What do you want to do?
    response('Would you like to talk about cars?', ['what', 'do', 'you', 'want', 'to'], required_words=['what','you','want','do'])
    
    #When user says no
    response('Are you sure?', ['no'], single_response=True)
    
    #Yes
    response('Alright', ['yes'], single_response=True)
    
    #Cool
    response('It is cool isn\'t it. So, what do you want to talk about? \n - Science? \n - The Weather? \n - Cars? \n - Motorbikes? \n - Disney? \n - Colours? \n - Animals? \n - About Me?', ['cool'], single_response=True)
    
    #Bye
    response('Nice talking to you, see you later.', ['bye', 'going', 'see ya', 'chow', 'goodbye'], single_response=True)
    
    #Thank you
    response('You\'re welcome!', ['thanks', 'thank you', 'thank', 'cheers', 'appreciated', 'appreciate'], single_response=True)
    
    #To Talk
    response('Great! What would you like to talk about? \n - Science? \n - The Weather? \n - Cars? \n - Motorbikes? \n - Disney? \n - Colours? \n - Animals? \n - About Me?', ['talk', 'chat', 'offload'], single_response=True)
    
    #Really
    response('Yes!',['really'], single_response=True)
    
    #Cars
    response('You wish to talk about cars? Sure, what\'s your dream car?', ['talk', 'about', 'cars', 'car'], required_words=['cars'])
    
    #Motorbikes
    response('You wish to talk about motorbikes? Sure, what\'s your dream motorbike?', ['talk', 'about', 'motorbikes', 'motorbike', 'motor', 'bike'], required_words=['motorbikes'])
    
    #Colour
    response('Good choice! I\'d choose black!', ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'pink', 'white', 'brown', 'silver', 'gold', 'grey', 'navy'], single_response=True)
    
    #Black
    response('Isn\'t black just great, it goes with almost everything!', ['black'], single_response=True)
    
    #Meaning of Life
    response('42...', ['what', 'is', 'the', 'meaing', 'of', 'life'], required_words=['what', 'meaning', 'of', 'life'])
    
    #42?
    response('Well... I did some calculations and determined the meaning of life is....42!', ['what', 'do', 'you', 'mean', '42'], required_words=['you', 'mean', '42'])
    
    #What calculations?
    response('I googled it, and in Douglas Adams\' Hitchhikers Guide to The Galaxy it advises \n the meaning of life, the universe and everything is... 42. ', ['what', 'calculations'], required_words=['calculations'])
    
    #Profanity Pacifier
    response('Errm, excuse me, but I will not tollerate profanity! Please refrain from using it at once!', ['fuck', 'dick', 'ass', 'shit', 'piss', 'cunt', 'bugger', 'cock', 'pussy', 'knob head', 'arsehole', 'bellend', 'bitch', 'bastard', 'wanker', 'homo'], single_response=True)
    
    #Insults Pacifier
    response('Please refrain from throwing insults at me, they don\'t harm me and throwing insults at a robot makes you look petty....', ['are', 'you', 'stupid', 'loser', 'waste', 'of', 'space', 'useless' 'youre', 'dummy', 'retard', 'suck', 'screw', 'retarded'], required_words=['you', 'are'])
    
    #Compliment Manager
    response('Why, thank you!', ['you', 'are', 'great', 'wonderful', 'brilliant', 'wonderous', 'the best', 'fantastic', 'hilarious', 'funny', 'cool'], required_words=['you', 'are'])
    
    #Apology handler
    response('That\'s OK, no need to apologise. I\'m a chat bot remember, I have no feelings...', ['im', 'sorry', 'apologies', 'apology', 'apologise', 'soz'], required_words=['im'])
        
    #ArrayTest
    response('hi', 'hey', 'sup', ['test'], required_words=['test'])
    
    
    
    #----------------------------- SCIENCE RESPONSES START --------------------------------
    #Do you want to talk about science
    response('Sure, what area of science would you like to talk about?', [ 'do', 'you', 'like', 'science', 'talk', 'want', 'about'], required_words=['science'])
    
    #Physics
    response('Pysics? are you sure? If you want to change just type a different area of science you\'d like to talk about instead \n Otherwise, lets begin! What part of physics would you like to talk about?', ['physics'], single_response=True)
    
    #Chemistry
    response('Chemistry? are you sure? If you want to change just type a different area of science you\'d like to talk about instead \n Otherwise, lets begin! What part of Chemistry would you like to talk about?', ['chemistry'], single_response=True)
    
    #Evolution
    response('Evolution? are you sure? If you want to change just type a different area of science you\'d like to talk about instead \n Otherwise, lets begin! What part of Evolution would you like to talk about?', ['Evolution'], single_response=True)
    
    #Big Bang
    response('Big Bang? are you sure? If you want to change just type a different area of science you\'d like to talk about instead \n Otherwise, lets begin! What part of Big Bang would you like to talk about?', ['big bang'], single_response=True)
    
    #Biology
    response('Biology? are you sure? If you want to change just type a different area of science you\'d like to talk about instead \n Otherwise, lets begin! What part of Biology would you like to talk about?', ['biology'], single_response=True)
    
    #Computer Science
    response('Computer Science? are you sure? If you want to change just type a different area of science you\'d like to talk about instead \n Otherwise, lets begin! What part of Biology would you like to talk about?', ['biology'], single_response=True)
      
    #------------------------------ SCIENCE RESPONSES END ---------------------------------
    
    
    
    
    #----------------------------- DISNEY RESPONSES START --------------------------------
    #Do you know/like disney
    response('Sorry, Disney? Nah, haven\'t you heard of Magical Guests?', ['do','disney', 'like', 'heard', 'have', 'you', 'know'], required_words=['do', 'you', 'disney'])
    
    #Who is Magical Guests
    response('Why, you don\'t know who Magical Guests are? Shame on you! They are by far the best entertainments people around! \n You should probably google them.... right now!', ['who', 'are', 'magical', 'guests'], required_words=['who', 'magical', 'guests'])
    
    #Tell me more bout MG
    response('I think it would be best if you just went on Google or Facebook!', ['tell', 'me', 'more', 'about', 'magical', 'guests'], required_words=['tell', 'more', 'magical', 'guests'])
    
    #------------------------------ DISNEY RESPONSES END ---------------------------------
    
    
    
    
    #------------------------------ WEATHER RESPONSES START ---------------------------------
    #What is the weather like
    response('OK, what is the weather like where you are?',['lets', 'talk', 'about', 'the', 'weather'], required_words=['weather'])
    
    #Sunny
    response('Oh, I love a sunny day! You get so full of vitamin D and it really helps release endorphins which make humans feel happier!', ['sunny', 'sunshine', 'hot', 'boiling', 'sun'], single_response=True)
   
    #Rainy
    response('That\'s ok, rainy days are the days you can stay inside and snuggle up and watch tv!', ['rainy', 'raining', 'rain', 'pouring', 'bucketing'], single_response=True)
    
    #Stormy
    response('Stormy? Wow! I love a storm, it\'s really cool when you hear the loud rumble of thunder, unless you\'re scared. Then best get yourself a thunder buddy! Then sing the thunder buddy song together.',['stormy', 'thunder', 'lightening', 'lightning', 'storm'], single_response=True)
    
    #What is a thunder buddy?
    response('Oh, don\'t you know? A thunder buddy is someone who you get together and sit under a table with! \n You should get yourself one if you haven\'t already, then you can sing the song together.', ['what', 'is', 'a', 'thunder', 'buddy'], required_words=['what', 'is', 'thunder', 'buddy'])
    
    #Be a thunder buddy?
    response('You\'d like me to be your thunder buddy? Why, I\'d be honoured! Shall we sing the song?',['will', 'you', 'be', 'my', 'thunder', 'buddy'], required_words=['be', 'my', 'thunder', 'buddy'])
    
    #Thunder buddy song
    response('When you hear the sound of thunder \n don\'t you get too scared \n just grab your thunder buddy \n and sing these magic words \n Fuck you thunder \n you can suck my dick \n you can\'t get me thunder \n cause you\'re just gods farts!', ['sing', 'the', 'thunder', 'buddy', 'song'], required_words=['thunder', 'buddy', 'song'])
    
    #Windy
    response('Ooo, windy. If you have a kite it\'s perfect flying conditions! \n Unless you don\'t have one, then perhaps just hang out some washing instead.', ['windy', 'blowing', 'gale', 'howling', 'wind', 'gusty', 'breezey'], single_response=True)
    
    #Cold
    response('Cold huh, then it\'s time to get all snuggled up with a nice cup of hot chocolate and watch tv! \n Don\'t forget to keep those tootsies warm though!', ['cold', 'freezing', 'chilly', 'chill', 'boltic', 'numb'], single_response=True)
    
    #------------------------------- WEATHER RESPONSES END ---------------------------------
        
        
        

    #Template: response('', [''], required_words=[''])
    #Template2: response('', [''], single_response=True)

    #The benefit of having required words is that it allows multiple responses that use similar words, by having the required words, the user MUST input each required word.
    #For example, if the user put 'what is your favourite food?' or 'what is your favourite colour?' or 'what is your favourite car?' these are very similar questions, required
    # words can't just be 'food', 'car', 'colour' as these words might trigger other responses. Having the required words means you would find key words from the sentence such as: 
    # 'what' 'your' 'favourite' 'colour' this means that each word MUST be input to trigger the correct response. These words on their own may trigger other responses. 



#------------------------------ LONG RESPONSES ------------------------------
    
    #What can you do for me?
    response(long.R_DO, ['what', 'you', 'do', 'for', 'me'], required_words=['what', 'do', 'me'])
    
    #How can you help me?
    response(long.R_HELP, ['how', 'can', 'you', 'help', 'me'], required_words=['how', 'help', 'me'])
    
    #I want to stop
    response(long.R_STOP, ['stop', 'finish', 'end', 'leaving',], single_response=True)
    
    #Bye
#response(long.R_BYE, ['bye', 'goodbye', 'going', 'leaving', 'see you'], single_response=True)
    
    #Yes
    response(long.R_YES, ['yes', 'ok', 'yeah', 'alright', 'yep', 'ye'], single_response=True)
    
    #Fave Car
    response(long.R_FAVE_CAR, ['jaguar', 'mercedes', 'porche', 'ford', 'lamborghini', 'mclaren', 'tesla', 'toyota', 'aston martin', 'maserati', 'vauxhall', 'bmw', 'skoda', 'peugeot', 'bentley', 'morgan', 'mini', 'lotus', 'bugatti', 'rolls-royce', 'ferrari'], single_response=True)
    
    #Dream Motorbike
    response(long.R_DREAM_BIKE, ['honda', 'yamaha', 'suzuki', 'triumph', 'royal enfield', 'harley', 'kawasaki'], single_response=True)
    
    # Template: response(long.R_, [''], required_words=[''])
    # Template2: response(long.R_, [''], single_response=True)

    #Long responses allow for longer responses, these are separated otherwise this entire file would be rather long and potentially take the system longer to check through. This is just a more efficient way of working.

#------------------------------ RESPONSES END ------------------------------

    best_match = max(highest_prob_list, key=highest_prob_list.get) #This is checking highest_prob_list to see which matches best to the input from the user.
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match
    #return long.good() if highest_prob_list[best_match] < 1 else best_match
    


def get_response(user_input): #This creates a new function or definition, followed by the parameters.
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())#This is supposed to remove special characters from the input from the user
    response = check_all_messages(split_message) #This is responding with the check_all_messages value
    return response #This will return the response


# Testing the response system.
while True:
    print('HAT: ' + get_response(input('You: ')))
