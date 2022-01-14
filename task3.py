import random


# Getting Started

def reply(question, name):#funtion for reply.
    if "library" in question.lower():
        print("The library is closed today.")
    elif "wifi" in question.lower():
        print("WiFi is excellent across the campus.")
    elif "deadline" in question.lower():
        print("Your deadline is extended by two working days.")
    elif "Coffee" in question.lower():
        print("The cafe in just beside the campus")
    elif "Cab" in question.lower():
        print("You can request for a cab from our campus website.")
    elif "Tour" in question.lower():
        print("The campus is helding a educational tour next weeek.")
    elif question.lower() in ["bye", "exit", "thanks", "help"]:
        exit(f"Thanks, {name}")
    else:
        print(random.choice(["Hmm.", "Oh, yes, I see.", "Tell me more.", "Is it?", "Good to know."]))#generating random words.




print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.\n")

email = input("Please enter your Poppleton email address : ")

if (email.count('@') == 1) and (email.split('@')[1] == "pop.ac.uk") and (len(email.split('@')[0]) >= 3):#checking the format.
    name = email.split('@')[0].capitalize()
    operator = random.choice(["Siri", "Fiona", "Alexa", "Friday", "John"])#choosing random operator.

    print(f"Hi {name}! Thank you, and Welcome to PopChat! ")
    print(f"My name is {operator},and it will be my pleasure to help you.")

    while True: 
        if random.choice([i for i in range(10)]) == 1:#creating network error with 10% probability
            print("*** NETWORK ERROR ***\n")
            exit(f"Thanks, {name}")
        question = input("---> ")
        reply(question, name)
