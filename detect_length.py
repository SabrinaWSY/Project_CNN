# Script for projet CNN TAL M2 Inalco 
# Author : Siyu WANG
# Detect length of wav files and remove files that are shorter than 0.8 seconds 

import wave
import contextlib
import os
import soundfile as sf

def remove_short_audio(langue):
    cnt = 0

    for file in os.listdir("./corpus_valide_chunk_nosilence/"+langue):
        if file.endswith('.wav'):
            fname = "./corpus_valide_chunk_nosilence/"+langue+'/'+file
            print(fname)

            with contextlib.closing(wave.open(fname,'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                print(duration)
                if duration < 0.8:
                    os.remove(fname)
                    print("removed :"+fname)
                    cnt+=1
    print(langue+": "+str(cnt))

#remove_short_audio("chinois")
#remove_short_audio("estonien")
#remove_short_audio("mongol")
remove_short_audio("tatar")