import xml.etree.ElementTree as ET
import csv


tree = ET.parse('obecnа_osoba.xml')
root = tree.getroot()


def parseXML():
    return



with open('export.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    OM_OBJECT = root.find(".//OM_OBJECT")
    ObjectID = OM_OBJECT.get('ObjectID')
    DirectoryID = OM_OBJECT.get('DirectoryID')
    TemplateName = OM_OBJECT.get('TemplateName')


    columns = ['ObjectID', 'DirectoryID', 'TemplateName']
    values = [ObjectID, DirectoryID, TemplateName]

    # Naplnim 
    for OM_FIELD in root.findall(".//OM_FIELD"):
        FieldID = OM_FIELD.get('FieldID')
        IsEmpty = OM_FIELD.get('IsEmpty')
        OM_STRING = OM_FIELD.find('./OM_STRING')
    
        if OM_STRING is None:
            value  = ''
        else:
            value = OM_STRING.text
        
        if value is None:
            value  = ''

        columns.append(FieldID)
        values.append(value)
    
    spamwriter.writerow(columns)
    spamwriter.writerow(values)


