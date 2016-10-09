Parseit
=======

`Parseit` es una herramienta de linea de comandos para "interpretar" archivos de texto con formato. 


### Requerimientos:
### Instalaci�n:
### Uso:

```
#!bash

Parseador de archivos
2016, Patricio Moracho <pmoracho@gmail.com>

argumentos posicionales:
  "archivo a interpretar"          Archivo de input

argumentos opcionales:
  -h, --help                       mostrar esta ayuda y salir
  -v, --version                    show program's version number and exit
  -f "path o archivo", --format "path o archivo"
                                   Definir path o archivo FMT a utilizar
  -u "formato", --useformat "formato"
                                   Forzar el uso de un determinado formato para porcesar el archivo
  -t, --dontusetables              No usar traducci�n por tablas y mostrar los datos nativos
  -s, --showformat                 Mostrar informaci�n de un formato (--format) en particular o todos los definidos
  -i, --ignorefmterror             Ignorar errores al cargar archivos de formatos
  -o "archivo", --outputfile "archivo"
                                   Exportar a un archivo
  -e "formato", --exportformat "formato"
                                   Exportar en un formato espec�fico
  -c "columnas", --showcols "columnas"
                                   N�meros de las columnas a mostrar
  -r "filas", --showrows "filas"   N�meros de las filas a mostrar
  -n, --dontshowrecordnumber       No mostrar los n�meros de cada registro
  -z, --horizontalmode             Modo de visualizaci�n horizontal

Ejemplos de uso:

- Interpretar un archivo infiriendo el formato:
  parseit [opciones] <archivo a interpretar>

- Mostrar todos los formatos disponibles y sus definiciones:
  parseit [opciones] -s [opciones]

- Mostrar esta ayuda:
  parseit -h
```

### Formatos
+ Los formatos se definene en uno o m�s archivos .FMT que no son m�s que archivos [JSON](http://www.json.org/)
+ [JSON Editor Online](http://www.jsoneditoronline.org/) Para validar la edici�n del archivo de formatos
 
### Changelog:
#### Version 0.1
* Versi�n inicial
