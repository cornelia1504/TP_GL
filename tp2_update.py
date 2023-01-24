#encoding : utf8
"""Mamitiana."""
import sys
import os
ADN_LIST=("A","C","G","T")
def fasta_read(fastafile):
    """fasta file control."""
    extension = os.path.splitext(fastafile) #verification de l'extension
    if extension == '.fasta':
        with open(fastafile,"r", encoding="utf-8") as file:
            lines = file.readlines()
            print(lines)
            chaine_fasta = ' '.join(lines)
            counter = 0
            header = ""
            prefix = ">" # Verification du contenu du fichier FASTA
            for i , prefix in enumerate(prefix):
                if chaine_fasta[i] != prefix[i]:
                    print("ErroR this is not a fasta file")
                    break
            else:
                for line in lines:
                    counter += 1
                    if line[0] == ">":
                        header = line.strip()
                    else: #faire l'operation sur les lignes autre que celui avec le chevron
                        line = line.strip()
                        line = line.upper()
                        column_counter = 0
                        for char in line:
                            column_counter += 1
                            if char not in ADN_LIST:
                                print( char  + " It's not a nucl in line " + str(counter) +
                                " and column " + str(column_counter)+ " for sequence "+header[1:])
    else :
        print("Error this is not a fasta file")
if __name__ == "__main__" :
    for arg in sys.argv[1:]:
        if os.path.exists(arg):
            fasta_read(arg)
        else:
            print(arg + "file doesn't exist")
