# Import the required module for text 
# to speech conversion
from gtts import gTTS
# This module is imported so that we can 
# play the converted audio
import os


def generate_audio(text, language='en', audio_file_name='output_audio_lara.mp3'):
    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save(audio_file_name)


def play_audio(audio_file_name='output_audio_lara.mp3'):
    # Playing the converted file
    os.system('mpg321 ' + audio_file_name)


generate_audio(text="I like the lunch here")
play_audio()
