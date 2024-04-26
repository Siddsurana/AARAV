import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from ShazamAPI import Shazam
from io import BytesIO

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to record voice and convert it to MP3
def record_and_convert_to_mp3():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Recognizing...")
        try:
            # Convert the recorded audio to text
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            speak("You said:" + text)
            # Convert the audio to MP3 format
            audio = AudioSegment.from_file(BytesIO(audio.get_wav_data()))
            audio.export("recorded_voice.mp3", format="mp3")
            return "recorded_voice.mp3"
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            speak("Sorry, I could not understand what you said.")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            speak("Could not request results from Google Speech Recognition service.")
            return None

# Function to recognize the song using Shazam
def recognize_song(file_path):
    try:
        shazam = Shazam.from_file(file_path)
        recognize_generator = shazam.recognizeSong()
        print("Recognizing song...")
        result = next(recognize_generator)
        print("Song recognized:", result['track']['title'], "by", result['track']['subtitle'])
        speak("Song recognized:" + result['track']['title'] + " by " + result['track']['subtitle'])
    except Exception as e:
        print("An error occurred:", str(e))
        speak("An error occurred while recognizing the song.")

# Main function
def main():
    mp3_file_path = record_and_convert_to_mp3()
    if mp3_file_path:
        recognize_song(mp3_file_path)

if __name__ == "__main__":
    main()
