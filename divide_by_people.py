from numpy import *
from pydub import AudioSegment

class Divider:
    def divide(self, filename, path):
        input = open('output.out')
        result = []
        wavfiles = []
        index = 1
        wavfile = AudioSegment.from_wav(filename)
        for line in input:
            temp = line.split(' ')
            speaker_info = temp[4]
            speaker_num = speaker_info[16:]
            result.append(int(speaker_num))
            start = temp[2]
            end = temp[3]
            start_info = start[11:]
            end_info = end[9:]
            start_time = float(start_info) * 1000
            end_time = float(end_info) * 1000
            f_name = str(index) + '.wav'
            wavfiles.append(f_name)
            _f = wavfile[start_time:end_time]
            _f.export(path + f_name, format="wav")
            index = index + 1
        return wavfiles, result


if __name__ == '__main__':
    data = Divider()
    data.divide('meeting.wav', './media/')
