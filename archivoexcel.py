import csv

import json


def csvToJson(file_in, file_out):

    data = []  # Creo una lista vacia

    with open(file_in, 'r') as csv_file:

        f_reader = csv.DictReader(csv_file)

        for row in f_reader:

            data.append(row)

            print(data)

    with open(file_out, 'w') as json_file:

        json.dump(data, json_file)

    print(f'Se ha transformado el archivo {file_in} y lo hemos exportado a {file_out}')
    
csvToJson('files/mail.csv', 'mail.json')

mail = open('files/mail.csv','r',encoding='utf8').readline()
mail