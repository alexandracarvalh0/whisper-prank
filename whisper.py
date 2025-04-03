import pyttsx3 
import random
import time 

engine = pyttsx3.init()
engine.setProperty('rate', 90) # Voice speed

phrases = [
    "I see you",
    "Im behind you",
    "Dont turn around",
    "Look at your camera",
    "Smile"
]

while True: 
    time.sleep(random.randint(10, 20)) # Timeout in seconds
    random_phrases = random.choice(phrases)
    engine.say(random_phrases)
    engine.runAndWait()