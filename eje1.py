import pandas as pd
import numpy as np

datos = {'Nombre':['Leonardo' , 'Joaquin','Alex','Paula','Enrique','Jhon'],
         'Materias':['Lenguaje','EDF','Matematicas','Quimica','Ingles','Historia'],
         'Calificaciones':['18','20','13','19','16','17'],
         'Deportes':['Futbol','Natacion','Tennis','Voley','Natacion','Balon Mano']}

df = pd.DataFrame(datos)
print(df)
print('\n'*4)


#DATOS NO VALIDOS
datos2 = {'Nombre':['Leonardo' , 'Joaquin','N/A','Paula','Enrique','Jhon'],
         'Materias':['Lenguaje','EDF','Matematicas','Quimica','Ingles','N/A'],
         'Calificaciones':['18','20',np.nan,'19','16','17'],
         'Deportes':['Futbol','Natacion','Tennis','Voley','N/A','Balon Mano']}

df2 = pd.DataFrame(datos2)
print(df2)
print('\n'*1)

print(df2.info())

#ESTADISTICAS BASICAS
print(df2.describe())
print('\n'*4)
nuevo = pd.DataFrame(df2)
nuevo = nuevo.replace(np.nan,"0")
print(nuevo);
print('\n'*4)

#ELIMINAR REGISTRO POR COLUMNA
columna = df2[df2['Nombre']!='N/A']
print(columna)

#CONVERTIR LOS NUMEROS A ENTEROS
df['Calificaciones'] = df.Calificaciones.astype(int)
print(df.describe())

#ESTADISTICAS INDIVIDUALES
print("Promedio:",df['Calificaciones'].mean())

