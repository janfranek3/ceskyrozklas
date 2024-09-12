# funkce vraci, zda existuje zaznam s neprazdnym jmenem pro dany objektID?
def rowWithNonEmptyNameExists(content, objectID):
    for line in content:
        if line[0] == objectID and line[1] != "":
            return True
    return False

# funkce vraci indexy zaznamu k odstraneni
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
        else:
            if line[1] == "":
                indices.append(index + 1)

    return indices