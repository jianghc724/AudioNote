from divide_by_people import Divider
from speech_to_text import Converter
from os import listdir
from os.path import isfile, join


class AudioNote:
    def getResult(self, path):
        d = Divider()
        c = Converter()
        speaker = d.divide()
        wavfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('wav')]
        index = 0
        for fn in wavfiles:
            text = c.convert(path + fn)
            print('Speaker ', speaker[index], ': ', text)
            index = index + 1

if __name__ == '__main__':
    data = AudioNote()
    data.getResult('./media/')
