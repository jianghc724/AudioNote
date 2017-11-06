from divide_by_people import Divider
from speech_to_text import Converter


class AudioNote:
    def getResult(self, filename, path):
        d = Divider()
        c = Converter()
        wavfiles, speaker = d.divide(filename, path)
        index = 0
        for fn in wavfiles:
            text = c.convert(path + fn)
            print('Speaker ', speaker[index], ': ', text)
            index = index + 1

if __name__ == '__main__':
    data = AudioNote()
    data.getResult('meeting.wav', './media/')
