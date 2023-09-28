LOS ADJETIVOS DEL HOMBRE VIRTUOSO
Ese cuerpo, señores, que con piadosos ojos estáis mirando, fue depositario de un alma en quien el cielo puso infinita parte de sus riquezas. 
Ese es el cuerpo de Grisóstomo, que fue único en el ingenio, solo en la cortesía, estremo en la gentileza, 
fénix en la amistad, magnífico sin tasa, grave sin presunción, alegre sin bajeza, y, finalmente,
primero en todo lo que es ser bueno, y sin segundo en todo lo que fue ser desdichado. Quiso bien, fue aborrecido; adoró, fue desdeñado;
rogó a una fiera, importunó a un mármol, corrió tras el viento, dio voces a la soledad, sirvió a la ingratitud,
de quien alcanzó por premio ser despojos de la muerte en la mitad de la carrera de su vida

pathquijote='file/quijote1.txt'
def wordcounter(file):
    with open(file,'r') as f:
        conted = f.read()
        word = conted.split()
        cant = len(word)
    return(cant)  
  
  
wordcounter(pathquijote)

 
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
    
csvToJson('mi_archivo.csv', 'elnew.json')