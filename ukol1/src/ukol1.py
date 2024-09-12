import csv

def  

# open .tsv file
with open("data_cleanup.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for line in tsv_file:
        print(line)