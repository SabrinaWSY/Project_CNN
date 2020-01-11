# Script for projet CNN TAL M2 Inalco 
# Author : Siyu WANG
# Choose validated audio files

import os
import csv
# importing shutil module  
import shutil 

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def extract_from_file(file_path, sep='\t'):
    """
    Extract data from csv file
    :param file_path: the csv file path
    :param sep: the separator string (default to '\t')
    :return : filepath
    """
    filepath = []

    with open(file_path) as f:
        premiere_ligne = f.readline() #eliminer la 1ere ligne
        file_reader = csv.reader(f, delimiter=sep)
        for row in file_reader:
            filepath.append(row[1])
            
    return filepath

def move(pathlist, destination, langue):
    for i in pathlist:
        source = find(i,"./Corpus/"+langue) 
        dest = shutil.move(source, destination)  
        print("Destination path:", dest)  

def main():
    paths_ch = extract_from_file('./Corpus/Chinois/validated.tsv')
    paths_es = extract_from_file('./Corpus/Estonien/validated.tsv')
    paths_mo = extract_from_file('./Corpus/Mongol/validated.tsv')
    paths_ta = extract_from_file('./Corpus/Tatar/validated.tsv')
    os.mkdir('./Corpus/chinois_valide')
    os.mkdir('./Corpus/estonien_valide')
    os.mkdir('./Corpus/mongol_valide')
    os.mkdir('./Corpus/tatar_valide')
    move(paths_ch,'./Corpus/chinois_valide','Chinois')
    move(paths_es,'./Corpus/estonien_valide','Estonien')
    move(paths_mo,'./Corpus/mongol_valide','Mongol')
    move(paths_ta,'./Corpus/tatar_valide','Tatar')
    
if __name__ == "__main__":
	main()


