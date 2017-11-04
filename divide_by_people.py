import scipy.io.wavfile as wav
import numpy as np
import speechpy
from os import listdir
from os.path import isfile, join
from extract_feature import Extract


class Divider:
    def divide(self, path):
        wavfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('wav')]
        cur_feature = []
        ex = Extract()
        total_speaker = 0
        for fn in wavfiles:
            feature, feature_cube = ex.extract(path + fn)
            min = 1
            avr_f = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            num_sample = 0
            for f in feature:
                avr_f = avr_f + f
                num_sample = num_sample + 1
            avr_f = avr_f / num_sample
            index = 0
            nearest_speaker = -1
            for cfc in cur_feature:
                dist = np.sqrt(np.sum(np.square(avr_f - cfc)))
                if dist < min:
                    nearest_speaker = index
                    min = dist
                index = index + 1
            if nearest_speaker != -1:
                print('Speaker', nearest_speaker + 1, 'speaking')
                cur_feature[nearest_speaker] = (cur_feature[nearest_speaker] + avr_f) / 2
            else:
                cur_feature.append(avr_f)
                total_speaker = total_speaker + 1
                print ('Speaker', total_speaker, 'speaking')
        print('Total speaker:', total_speaker)
        print(cur_feature)

if __name__ == '__main__':
    data = Divider()
    data.divide('./media/')
