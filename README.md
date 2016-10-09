Parseit
=======

`Parseit` es una herramienta de linea de comandos para "interpretar" archivos de texto con formato. Algunos puntos claves de este proyecto:

* Herramienta de línea de comandos
* Interpretación de archivos de texto de formato especifico, con caracter de fin de línea. Más adelante veremos como manejar otros formatos.
* Uso de archivos JSON para la definición del formato (consultar parseit.json)
	* Definicón de campos, longitudes y formatos varios
	* Definción de valores tipo tabla (codigo: valor) para reemplazo al mostrar de los mismos
* Especificación de un formato determinado o por defecto el archivo "parseit.fmt" que estuviera en la misma carpeta de ejecutable
* Varios formatos de exportación de los datos, entre otros:
	* psql 
	* csv
	* html
	* etc.
* Definir que filas y que columnas mostrar
* Útil visualización o "transposición" de la tabla al modo "horizontal"
* Poder incorporar un hoja de estilos cuando los datos los mostramos en html
* Poder exportar a un archivo determinado y apertura automática del mismo
* Con la distribución se distribuyen los formatos para interpretar los archivos de texto para el Siap / Afip:
	* **ARCIBA**: debitos y créditos
	* **RG3685**: Compras: comprobantes y alicuotas, Ventas: comprobantes y alicuotas
	* **SIFERE**: Retenciones y percepciones
	* **SICORE**: Retenciones y percepciones


### Requerimientos e instalación:

En Windows, nada en particular ya que se distribuye la herramienta "congelada" mediante **Pyinstaller**. Descargarla y copiarla en alguna carpeta del sistema, idealmente que este apuntada al path.

* Para descargar y descomprimir **Parseit**, hacer click [aqui](https://bitbucket.org/pmoracho/python.projects/raw/bd19d803a17e2fe6720fc603117a75d2cd1c6b76/parse/dist/parseit-20160606.zip)
* El proyecto en [**Bibucket**](https://bitbucket.org/pmoracho/python.projects/src/0805fe4eed49/parse/?at=master)


### Uso:

```
#!bash

uso: parseit [-h] [-v] [-f "path o archivo"] [-u "formato"] [-t] [-s] [-i]
             [-o "archivo"] [-x] [-e "formato"] [-c "columnas"] [-r "filas"]
             [-n] [-z] [-a] [-l "archivo css"]
             ["archivo a interpretar"]

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
  -x, --openfile                   abrir automáticamente el archivo
  -e "formato", --exportformat "formato"
                                   Exportar en un formato específico
  -c "columnas", --showcols "columnas"
                                   Números de las columnas a mostrar
  -r "filas", --showrows "filas"   Números de las filas a mostrar
  -n, --dontshowrecordnumber       No mostrar los números de cada registro
  -z, --horizontalmode             Modo de visualización horizontal
  -a, --addtotals                  Agregar una última fila con los totales de los campos númericos
  -l "archivo css", --css-file "archivo css"
                                   Archivo de estilos (.Css) para la salida Html

Ejemplos de uso:

- Interpretar un archivo infiriendo el formato:
  parseit [opciones] <archivo a interpretar>

- Mostrar todos los formatos disponibles y sus definiciones:
  parseit [opciones] -s [opciones]

- Mostrar esta ayuda:
  parseit -h  
```

### Formatos
+ Los formatos se definen en uno o más archivos .FMT que no son más que archivos [JSON](http://www.json.org/)
+ [JSON Editor Online](http://www.jsoneditoronline.org/) Para validar la edición del archivo de formatos


### Changelog:

#### Version 1.1
* Primer release oficial de la herramienta
* Se distribuyen varios formatos para interpretar archivos de Afip / Siap

#### Version 0.1
* Versión inicial
