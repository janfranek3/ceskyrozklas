import os
import csv
from mylib import *

# open .tsv file
with open(os.path.dirname(__file__) + '/../../data_cleanup.tsv') as file:
    content = csv.reader(file, delimiter="\t")
    
    # Nactu si cely soubor do promenne contentInMemory
    contentInMemory = []    
    for line in content:
        contentInMemory.append(line)

    # vypisu indexy radku k odstraneni
    print(rowIndicesToRemove(contentInMemory))