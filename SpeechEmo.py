import speech_recognition as sr
from TextEmo import textemo
from subprocess import call

def speechemo():
    # obtain audio from the microphone
    pathToFileInDisk = r'./data/test.wav'

    # call(["./Record"],shell=True)
    print "start"
    r = sr.Recognizer()
    with sr.AudioFile(pathToFileInDisk) as source:
        audio = r.listen(source)
    print "start analyze"
        # recognize speech using Microsoft Bing Voice Recognition
    BING_KEY = "7c9c086e169449e5bb48e6fb5ecc52b6" 
    result = r.recognize_bing(audio, key=BING_KEY)
    try:
        print result
        return textemo(result)
    except sr.UnknownValueError:
        return "Microsoft Bing Voice Recognition could not understand audio"
    except sr.RequestError as e:
        return "Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e)


