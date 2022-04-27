#-----------------------------------------------------------------------------------------
# @Autor: Aurélien Vannieuwenhuyze
# @Empresa: Junior Makers Place
# @Libro
# @Capítulo: 03 - Estadísticas para comprender los datos
#
# Módulos necesarios:
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#   JMPEstadísticas (copiar el archivo dentro de su proyecto al mismo nivel que este archivo)
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------

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