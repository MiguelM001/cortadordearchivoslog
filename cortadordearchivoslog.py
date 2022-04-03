#########################################################################################
# NOTA 1:
#!/usr/bin/env python
#
# -*- coding: utf-8 -*- 
#
# TITULO: HERRAMIENTA PARA CORTAR ARCHIVOS LOGS EXTREMADAMENTE GRANDES, EN VARIOS ARCHIVOS MAS PEQUEÑOS
#
# SUSCERTE: VENCERT
# DEPARTAMENTO DE SEGURIDAD LOGICA
# AUTOR: MIGUEL MARQUEZ 
# CARACAS, DICIEMBRE DEL 2017
#
# cortadordearchivoslog.py V 1.0
#
#

#########################################################################################
# preguntar si es directorio
# caso cierto:
# buscar la ultima barra ejemplo /../../archivo.log
# despejar nombre de archivo archivo.log, copiar hasta ultimo punto, 
# resultado: "archivo"
# seran los nombres de archivos resultantes: archivo1, archivo2, archivo3
#########################################################################################
# NOTA 2:
# crear un estimado en tiempo dividiendo el tamaño de archivo entre el el tamaño del peso 
# ejemplo: archivo de 99 GB entre / 500 MB para eso debo convertir y redondear 
# me dara resultado la cantidad de veces que debe imprimir
#########################################################################################

archivo = open("eve.json", "r")

contenido= archivo.read(502400000)#500 MB escritos en bytes
print("1")

escribirArchivo=open('archivo1.json','w')
escribirArchivo.close()

escribirArchivo=open('archivo1.json','a')
escribirArchivo.write(contenido)
escribirArchivo.close()

cont= 2

while contenido:
    
    contenido= archivo.read(502400000)#500 MB
    print(cont)

    escribirArchivo=open('archivo'+str(cont)+'.json','w')
    escribirArchivo.close()

    escribirArchivo=open('archivo'+str(cont)+'.json','a')
    escribirArchivo.write(contenido)
    escribirArchivo.close()
    cont+= 1

