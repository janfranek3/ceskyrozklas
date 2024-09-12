import os
import csv

# funkce - existuje zaznam s neprazdnym jmenem pro dany objektID?
def rowWithNonEmptyNameExists(content, objectID):
    for line in content:
        if line[0] == objectID and line[1] != "":
            return True
    return False

def rowIndicesToRemove(content):

    # ObjectIDs, ktere maji pouze prazdna jmena
    objectIDsWithEmptyName = [] 

    # Indexy radku k odstraneni
    indices = []

    # hledam radky k odstraneni
    for index, line in enumerate(content):
        if rowWithNonEmptyNameExists(content, line[0]) == False:
            if line[0] in objectIDsWithEmptyName:
                # radek druhy a nasledujici objekt s prazdnym jmenem oznacim k odstraneni
                indices.append(index + 1)
            else:
                # prvni objekt s prazdnym jmenem musi zustat
                objectIDsWithEmptyName.append(line[0])

    return indices

# open .tsv file
with open(os.path.dirname(__file__) + '/../../data_cleanup.tsv') as file:
    content = csv.reader(file, delimiter="\t")
    
    # Nactu si cely soubor do promenne contentInMemory
    contentInMemory = []    
    for line in content:
        contentInMemory.append(line)

    # vypisu indexy radku k odstraneni
    print(rowIndicesToRemove(contentInMemory))