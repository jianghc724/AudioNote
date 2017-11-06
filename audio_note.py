from divide_by_people import Divider
from speech_to_text import Converter


class AudioNote:
    def getResult(self, filename, path):
        d = Divider()
        c = Converter()
        wavfiles, speaker = d.divide(filename, path)
        index = 0
        f = open("out.txt", "w")
        for fn in wavfiles:
            text = c.convert(path + fn)
            f.write('Speaker ')
            f.write(str(speaker[index]))
            f.write(': ')
            for t in text:
                f.write(t)
            f.write('\n')
            index = index + 1

if __name__ == '__main__':
    data = AudioNote()
    data.getResult('meeting.wav', './media/')
