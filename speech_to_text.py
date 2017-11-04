import speech_recognition as sr
import scipy.io.wavfile as wav
import numpy as np
import os


class Converter:
    def convert(self, file_name):
        r = sr.Recognizer()
        with sr.AudioFile(file_name) as source:
            audio = r.record(source)
        print("start recognize")

#        try:
#            print("Sphinx thinks you said "+ r.recognize_sphinx(audio, language='zh-CN'))
#        except sr.UnknownValueError:
#            print("Sphinx could not understand audio")
#        except sr.RequestError as e:
#            print("Sphinx error; {0}".format(e))

#        try:
#            print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='zh-CN'))
#        except sr.UnknownValueError:
#            print("Google Speech Recognition could not understand audio")
#        except sr.RequestError as e:
#            print("Could not request results from Google Speech Recognition service; {0}".format(e))

#        IBM_USERNAME = "38de5d99-7cf7-445a-ab1a-b138b98cbb86"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
#        IBM_PASSWORD = "VFdRan6vNf3P"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
#        try:
#            print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME,
#                                                                          password=IBM_PASSWORD, language='zh-CN'))
#        except sr.UnknownValueError:
#            print("IBM Speech to Text could not understand audio")
#        except sr.RequestError as e:
#            print("Could not request results from IBM Speech to Text service; {0}".format(e))

        GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"abc"
        try:
            print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio,
                                                                                    credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))


if __name__ == '__main__':
    data = Converter()
    data.convert('recording.wav')