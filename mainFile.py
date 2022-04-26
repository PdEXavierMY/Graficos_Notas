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


from cmath import nan
from os import sep
import pandas as pd
import JMPEstadisticas as jmp
import numpy as np

#--- CREACION DE UN DATAFRAME ----
def conseguirnotas():
    notas = pd.read_csv("data.csv", encoding = "UTF8", sep = ",")
    sem1, sem2, sem3, sem4, sem5 = [], [], [], [], []
    for valor in notas["1st"]:
        if valor == nan:
            valor = 0
            sem1.append(valor)
        else:
            sem1.append(valor)
    for valor in notas["2nd"]:
        if valor == nan:
            valor = 0
            sem2.append(valor)
        else:
            sem2.append(valor)
    for valor in notas["3rd"]:
        if valor == nan:
            valor = 0
            sem3.append(valor)
        else:
            sem3.append(valor)
    for valor in notas["4th"]:
        if valor == nan:
            valor = 0
            sem4.append(valor)
        else:
            sem4.append(valor)
    for valor in notas["5th"]:
        if valor == nan:
            valor = 0
            sem5.append(valor)
        else:
            sem5.append(valor)
    return sem1, sem2, sem3, sem4, sem5

notas1, notas2, notas3, notas4, notas5 = conseguirnotas()
print(notas1)
print(notas2)
#observaciones1, observaciones2, observaciones3, observaciones4, observaciones5 = pd.DataFrame({'NOTAS':np.array(notas1)}), pd.DataFrame({'NOTAS':np.array(notas2)}), pd.DataFrame({'NOTAS':np.array(notas3)}), pd.DataFrame({'NOTAS':np.array(notas4)}), pd.DataFrame({'NOTAS':np.array(notas5)})
#observaciones = pd.DataFrame({'NOTAS':np.array([3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16])})

#--- ANALISIS DE UNA CARACTERISTICA ---
#stats1, stats2, stats3, stats4, stats5 = jmp.JMPEstadisticas(observaciones1['NOTAS']), jmp.JMPEstadisticas(observaciones2['NOTAS']), jmp.JMPEstadisticas(observaciones3['NOTAS']), jmp.JMPEstadisticas(observaciones4['NOTAS']), jmp.JMPEstadisticas(observaciones5['NOTAS'])
#stats1.analisisCaracteristica()
#stats2.analisisCaracteristica()
#stats3.analisisCaracteristica()
#stats4.analisisCaracteristica()
#stats5.analisisCaracteristica()