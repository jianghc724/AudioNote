import scipy.io.wavfile as wav
import numpy as np
from numpy import *
import speechpy
from os import listdir
from os.path import isfile, join
from extract_feature import Extract


class Divider:
    def divide(self):
        input = open('output.out')
        result = []
        for line in input:
            temp = line.split(' ')
            speaker_info = temp[4]
            speaker_num = speaker_info[16:]
            result.append(int(speaker_num))
        print(result)
        return result


if __name__ == '__main__':
    data = Divider()
    data.divide()
