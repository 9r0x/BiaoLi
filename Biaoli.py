from ImgEmo import imgemo
from TextEmo import textemo
import speech_recognition as sr

i_result = 0
s_result = 0
print "Please speak"
i_result = imgemo()
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    i_result = (imgemo()+i_result)
    BING_KEY = "7c9c086e169449e5bb48e6fb5ecc52b6"
    s_result = textemo(r.recognize_bing(audio, key=BING_KEY))-0.5

i_result = (imgemo()+i_result)/3
print i_result
print s_result
if s_result*i_result>0 :
    print "Same"
else :
    print "Diff"
