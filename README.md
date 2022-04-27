# Graficos_Notas

Link de Kaggle al [csv](https://www.kaggle.com/datasets/sankha1998/student-semester-result)

Link al [repositorio](https://github.com/Xavitheforce/Graficos_Notas)
***

En este ejercicio he reutilizado el código proporcionado con las funciones necesarias para calcular una estadística de datos(media, moda, mediana, cuartiles) a partir de un dataset panda. Simplemente he ajustado el main para que reciba un csv(link en la parte superior) y saque las columnas que interesan en forma de lista. A partir de esa lista, pandas crea un dataset y lo pasa por el archivo JMPEstadísticas.

En este caso, el dataset contiene (entre otras) 5 columnas con las notas semestrales de x alumnos. El código está planteado para que si hubiera filas en blanco con algún dato en lo referente a esas notas, esas filas sean eliminadas y no den problemas. Además, la agregación de una función que calcula la media final(considerando que todo tiene el mismo peso) de las notas semestrales de los alumnos, y luego saca su estadística correspondiente, es original.

Este es el código del main adaptado a este ejercicio:

```python
import pandas as pd
import JMPEstadisticas as jmp
import numpy as np
from introducir import solicitar_introducir_numero_extremo

#--- CREACION DE UN DATAFRAME ----
def conseguirnotas():
    notas = pd.read_csv("data.csv", encoding = "UTF8", sep = ",")
    notas = notas.dropna(subset=["1st"])
    notas = notas.dropna(subset=["2nd"])
    notas = notas.dropna(subset=["3rd"])
    notas = notas.dropna(subset=["4th"])
    notas = notas.dropna(subset=["5th"])
    sem1, sem2, sem3, sem4, sem5 = list(notas["1st"]), list(notas["2nd"]), list(notas["3rd"]), list(notas["4th"]), list(notas["5th"])
    return sem1, sem2, sem3, sem4, sem5

notas1, notas2, notas3, notas4, notas5 = conseguirnotas()
def notasfinales(s1, s2, s3, s4, s5):
    notasmedia = []
    for i in range(len(s1)-1):
        total = float(s1[i])+float(s2[i])+float(s3[i])+float(s4[i])+float(s5[i])
        media = round((total/5), 2)
        notasmedia.append(media)
    return notasmedia
medias = notasfinales(notas1, notas2, notas3, notas4, notas5)
observaciones1, observaciones2, observaciones3, observaciones4, observaciones5, observacionestotales = pd.DataFrame({'NOTAS':np.array(notas1)}), pd.DataFrame({'NOTAS':np.array(notas2)}), pd.DataFrame({'NOTAS':np.array(notas3)}), pd.DataFrame({'NOTAS':np.array(notas4)}), pd.DataFrame({'NOTAS':np.array(notas5)}), pd.DataFrame({'NOTAS':np.array(medias)})

#--- Main ---
if __name__ == "__main__":
    eleccion = solicitar_introducir_numero_extremo("Elige de que semetre quieres la estadística(1-5), o si la quieres de una media de cada semestre(6)", 1, 6)
    stats1, stats2, stats3, stats4, stats5, statsfinales = jmp.JMPEstadisticas(observaciones1['NOTAS']), jmp.JMPEstadisticas(observaciones2['NOTAS']), jmp.JMPEstadisticas(observaciones3['NOTAS']), jmp.JMPEstadisticas(observaciones4['NOTAS']), jmp.JMPEstadisticas(observaciones5['NOTAS']), jmp.JMPEstadisticas(observacionestotales['NOTAS'])
    if eleccion == 1:
        stats1.analisisCaracteristica()
    elif eleccion == 2:
        stats2.analisisCaracteristica()
    elif eleccion == 3:
        stats3.analisisCaracteristica()
    elif eleccion == 4:
        stats4.analisisCaracteristica()
    elif eleccion == 5:
        stats5.analisisCaracteristica()
    elif eleccion == 6:
        statsfinales.analisisCaracteristica()
```
