import speech_recognition as sr


class Recorder:
    def record(self, path, filename):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        with open(path + filename, "wb") as f:
            f.write(audio.get_wav_data())

if __name__ == '__main__':
    data = Recorder()
    data.record('./media/', 'test.wav')
