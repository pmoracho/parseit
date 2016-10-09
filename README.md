Parseit
=======

`Parseit` es una herramienta de linea de comandos para "interpretar" archivos de texto con formato. 


### Requerimientos:
### Instalación:
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
  -t, --dontusetables              No usar traducción por tablas y mostrar los datos nativos
  -s, --showformat                 Mostrar información de un formato (--format) en particular o todos los definidos
  -i, --ignorefmterror             Ignorar errores al cargar archivos de formatos
  -o "archivo", --outputfile "archivo"
                                   Exportar a un archivo
  -e "formato", --exportformat "formato"
                                   Exportar en un formato específico
  -c "columnas", --showcols "columnas"
                                   Números de las columnas a mostrar
  -r "filas", --showrows "filas"   Números de las filas a mostrar
  -n, --dontshowrecordnumber       No mostrar los números de cada registro
  -z, --horizontalmode             Modo de visualización horizontal

Ejemplos de uso:

- Interpretar un archivo infiriendo el formato:
  parseit [opciones] <archivo a interpretar>

- Mostrar todos los formatos disponibles y sus definiciones:
  parseit [opciones] -s [opciones]

- Mostrar esta ayuda:
  parseit -h
```

### Formatos
+ Los formatos se definene en uno o más archivos .FMT que no son más que archivos [JSON](http://www.json.org/)
+ [JSON Editor Online](http://www.jsoneditoronline.org/) Para validar la edición del archivo de formatos
 
### Changelog:
#### Version 0.1
* Versión inicial
