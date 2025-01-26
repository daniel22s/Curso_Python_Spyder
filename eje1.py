import pandas as pd
import numpy as np

datos = {'Nombre':['Leonardo' , 'Joaquin','Alex','Paula','Enrique','Jhon'],
         'Materias':['Lenguaje','EDF','Matematicas','Quimica','Ingles','Historia'],
         'Calificaciones':['18','20','13','19','16','17'],
         'Deportes':['Futbol','Natacion','Tennis','Voley','Natacion','Balon Mano']}

df = pd.DataFrame(datos)
print(df)