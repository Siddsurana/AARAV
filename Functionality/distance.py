from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def find_location(city_name):
    geolocator = Nominatim(user_agent="location_finder")
    location = geolocator.geocode(city_name)
    if location:
        return {
            "city": location.address.split(",")[0],
            "state": location.raw.get('address', {}).get('state', ''),
            "country": location.raw.get('address', {}).get('country', ''),
            "latitude": location.latitude,
            "longitude": location.longitude
        }
    else:
        return None

def get_distance(current_location, target_location):
    if current_location and target_location:
        current_coords = (current_location["latitude"], current_location["longitude"])
        target_coords = (target_location["latitude"], target_location["longitude"])
        return geodesic(current_coords, target_coords).kilometers
    else:
        return None

def distance(query):
    pune_location = {"city": "Pune", "latitude": 18.604072319693284, "longitude": 73.756311868149}

    target_city_name = query
    target_location = find_location(target_city_name)

    if target_location:
        distance = get_distance(pune_location, target_location)
        print(f"The distance from Pune to {target_location['city']} is approximately {distance:.2f} kilometers.")
        speak(f"The distance from Pune to {target_location['city']} is approximately {distance:.2f} kilometers.")
    else:
        print("Sorry, could not find location information for the target city.")
        speak("Sorry, could not find location information for the target city.")





