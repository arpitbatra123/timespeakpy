from datetime import datetime
import pyttsx3


def convert24to12(hours):
    if hours > 12:
        return hours-12
    else:
        return hours


def speaktime(textToSpeak):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(textToSpeak)
    engine.runAndWait()


currdatetimeobj = datetime.now()

hours = currdatetimeobj.hour

if hours > 12:
    whatisthewordforAMorPM = "PM"
else:
    whatisthewordforAMorPM = "AM"


hours = convert24to12(hours)

minutes = currdatetimeobj.minute


print("The time is {} {} {}".format(
    hours, minutes, whatisthewordforAMorPM))

currTime = "The time is {} {} {}".format(
    hours, minutes, whatisthewordforAMorPM)

speaktime(currTime)
