# import pyttsx3

# engine = pyttsx3.init()

# worker_list = ['Zakkir', 'Kabeer', 'Talha', 'Ehsan']

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 50)  # speaking speed

# for item in worker_list:
#     text = f"Shout out to {item}, he did the program"
#     print(text)
#     engine.say(text)

# engine.runAndWait()
# engine.stop()


#SECOND METHOD

from gtts import gTTS
import os
my_text="shout out to Zakir he is good boy"

lan='en'

my_obj=gTTS(text=my_text,lang=lan,slow=True)
my_obj.save('name.mp3')
os.system('name.mp3')