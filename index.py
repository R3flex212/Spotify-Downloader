from pydub import AudioSegment
from os import listdir
import numpy as np
import math
import os



song_dir = "songs"
downloads_path = os.path.expanduser("~")+"/Downloads/"


def bass_line_freq(track):
    sample_track = list(track)

    # c-value
    est_mean = np.mean(sample_track)

    # a-value
    est_std = 3 * np.std(sample_track) / (math.sqrt(2))

    bass_factor = int(round((est_std - est_mean) * 0.005))

    return bass_factor

def run(accentuate_db,attenuate_db):
    for filename in listdir(song_dir):
        sample = AudioSegment.from_file(song_dir + "/" + filename)
        filtered = sample.low_pass_filter(bass_line_freq(sample.get_array_of_samples()))

        combined = (sample - attenuate_db).overlay(filtered + accentuate_db)
        combined.export(downloads_path + filename, format="mp3")



