from pydub import AudioSegment
from pydub.silence import split_on_silence

sound = AudioSegment.from_file("sample.mp3", "mp3")

chunks = split_on_silence(
    sound, 
                          min_silence_len = 100,
                          silence_thresh = -35,
                          keep_silence = 100)

cutted_sound = sum(chunks)
cutted_sound.export('cutted.mp3')