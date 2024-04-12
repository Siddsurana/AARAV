import pyttsx3
import smtplib
import speech_recognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def send_email(sender_email, sender_password, recipent_email, subject, content):
    from email.message import EmailMessage
    msg = EmailMessage()
    msg['from'] = sender_email
    msg["to"] = recipent_email
    msg["subject"] = subject
    msg.set_content(content)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()

    print("Email Sent Successfully")
    speak("Email Sent Successfully")

recipent_mapping = {
    "sahil" : "arankallesahil@gmail.com",
    "shounak" : "shounaksanpurkar@gmail.com",
    "loukik" : "loukiksancheti1928@gmail.com",
    "siddharth" : "siddharthsurana2605@gmail.com"
}

sender_email = "arankallesahil@gmail.com"
sender_password = "lsel orww ahof wkex"


