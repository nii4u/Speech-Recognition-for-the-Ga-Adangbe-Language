from glob import glob 
import os
path = "/home/thompson/Documents/Speech-Recognition-for-the-Ga-Adangbe-Language/DATA"

for portion in ['train', 'test', 'validation']:
    folders = os.listdir(os.path.join(path,portion))
    for folder in folders:
        np_audios = len(glob(os.path.join(path, portion, folder)+'/*.wav'))
        # print(os.path.join(path, portion, folder))
        # print(glob(os.path.join(path, portion, folder)+'/*linker.txt')[0]
        linker = open(glob(os.path.join(path, portion, folder)+'/*linker.txt')[0], 'r')
        np_lines_lr = len([line for line in linker.readlines()])
        if np_audios != np_lines_lr:
            print(os.path.join(path, portion, folder), 'np_audios:', np_audios, 'np_lines_lr:', np_lines_lr)

#200627-234031_gaa_980_elicit
#200628-002514_gaa_980_elicit
#200628-002514_gaa_980_elicit
#200627-234031_gaa_980_elicit 