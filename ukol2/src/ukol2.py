import xml.etree.ElementTree as ET
import csv
import argparse
import os
import json

# export do json
def output_json(output_file, columns, values):
    with open(os.path.dirname(__file__) + '/'+output_file, 'w', newline='') as file:
        
        output = {}
        for i, column in enumerate(columns):
            output[column] = values[i]
        
        json.dump(output, file)

# export do csv
def output_csv(output_file, columns, values):
    with open(os.path.dirname(__file__) + '/'+output_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columns)
        writer.writerow(values)

# export do tsv
def output_tsv(output_file, columns, values):
    with open(os.path.dirname(__file__) + '/'+output_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columns)
        writer.writerow(values)        

# funkce zparsuje vstupni xml a vrati pole sloupcu a hodnot
def parse_xml(input_file):

    tree = ET.parse(os.path.dirname(__file__) + '/'+input_file)
    root = tree.getroot()

    OM_OBJECT = root.find(".//OM_OBJECT")
    ObjectID = OM_OBJECT.get('ObjectID')
    DirectoryID = OM_OBJECT.get('DirectoryID')
    TemplateName = OM_OBJECT.get('TemplateName')

    columns = ['ObjectID', 'DirectoryID', 'TemplateName']
    values = [ObjectID, DirectoryID, TemplateName]

    # Naplnim 
    for OM_FIELD in root.findall(".//OM_FIELD"):
        FieldID = OM_FIELD.get('FieldID')
        OM_STRING = OM_FIELD.find('./OM_STRING')
    
        if OM_STRING is None:
            value  = ''
        else:
            value = OM_STRING.text
        
        if value is None:
            value  = ''

        columns.append(FieldID)
        values.append(value)
        
    return [columns, values]
        

# Hlavni funkce programu, ktera se spusti ihned jako prvni po spusteni
def main():

    # Zpracovani vstupnich parametru programu
    parser = argparse.ArgumentParser(
                        prog='2. Úkol',
                        description='XML transformace',
                        epilog='')

    parser.add_argument('source_file')
    parser.add_argument('--output_file')
    parser.add_argument('--otype')

    args = parser.parse_args()

    if os.path.isfile(args.source_file) == False:
        raise Exception("Input file does not exist")

    if args.output_file is not None:
        output_file_name = args.output_file
    else:
        output_file_name = os.path.basename(args.source_file).split('.')[0]

    # Zparsovani vstupniho xml
    parsed_xml = parse_xml(args.source_file)

    # Export do prislusneho formatu
    if args.otype == 'tsv':
        output_tsv(output_file_name+'.output.tsv', parsed_xml[0], parsed_xml[1])
    elif args.otype == 'json':
        output_json(output_file_name+'.output.json', parsed_xml[0], parsed_xml[1])
    else:
        output_csv(output_file_name+'.output.csv', parsed_xml[0], parsed_xml[1])



main()
