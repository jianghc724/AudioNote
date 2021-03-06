import scipy.io.wavfile as wav
import speechpy


class Extract:
    def extract(self, file_name):
        fs, signal = wav.read(file_name)
#        print(file_name)
        signal = signal[:, 0]
        mfcc = speechpy.mfcc(signal, sampling_frequency=fs, frame_length=0.020, frame_stride=0.01,
                             num_filters=40, fft_length=512, low_frequency=0, high_frequency=None)
        #print(mfcc.shape)
        #print(mfcc)
        mfcc_feature_cube = speechpy.extract_derivative_feature(mfcc)
        #print('mfcc feature cube shape:' , mfcc_feature_cube.shape)
        #print(mfcc_feature_cube)
        return mfcc, mfcc_feature_cube

if __name__ == '__main__':
    data = Extract()
    data.extract('recording.wav')