import csv

with open("glpi.csv","r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    print(arquivo_csv)
    for line in arquivo_csv
        print(line)
