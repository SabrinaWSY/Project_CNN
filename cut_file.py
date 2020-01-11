# Script for projet CNN TAL M2 Inalco 
# Author : Siyu WANG
# Cut mp3 files to chunks of 2 seconds and export in format .wav

import os
from pydub import AudioSegment
from pydub.utils import make_chunks

def cut_audio(langue):
    path = "./corpus_valide_sans_silence/"+langue+'/'

    for file in os.listdir("./corpus_valide_sans_silence/"+langue):
        myaudio = AudioSegment.from_file(path+file , "wav") 
        chunk_length_ms = 2000 # pydub calculates in millisec
        chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

    #Export all of the individual chunks as wav files

        for i, chunk in enumerate(chunks):
            chunk_name = "{0}chunk{1}.wav".format(path+file,i)
            print ("exporting", chunk_name)
            chunk.export(chunk_name, format="wav")

cut_audio("chinois")
cut_audio("mongol")
cut_audio("tatar")
cut_audio("estonien")