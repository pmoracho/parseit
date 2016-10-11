Parseit
=======

`Parseit` es una herramienta de linea de comandos para "interpretar" archivos de texto con formato. 

Para entender que es `parseit` nada mejor que un ejemplo práctico. Para el intercambio de información con el Afip, se 
suele trabajar con este tipo de archivos, en particular los contribuyentes grandes, que suelen generar gran cantidad
de información, veamos un caso típico, el Sistema federal de información más conocido domo **SIFERE** permite
importar masivamente la información de retenciones y percepciones, la información se arma en archivos de texto, 
con campos de lóngitud fija y caracteres de fin de linea:

```
90130-00000000-901/01/200612341234567891234560FA0000000000010000123500000125,20
90130-00000000-901/01/200612341234567891234560FA0000000000010000123500000125,20
90130-00000000-901/01/200612341234567891234560FA0000000000010000123500000125,20
```

Para poder interpretar este archivo, se "define" el formato en una archivo JSON, por ejemplo asi:

```
		"sifere-retenciones": {
			"category": "Afip.Sifere",
			"delimiter": "",
			"fields": {
				"Código de Jurisdicción" : 													[ 3, "table", "sifere-jurisdicciones", ""],
				"CUIT del Agente de Retención" : 											[13, "string", "", ""],
				"Fecha de la Retención" : 													[10, "date", "%d/%m/%Y", "%d-%m-%Y"],
				"Número de Sucursal" :	 													[ 4, "string", "", ""],
				"Número de constancia" :													[16, "string", "", ""],
				"Tipo de Comprobante" :														[ 1, "table", "sifere-tipo-comprobantes", ""],
				"Letra del Comprobante" :													[ 1, "string", "", ""],
				"Número de Comprobante Original" :											[20, "string", "", ""],
				"Importe Retenido" :														[11, "amount", "", ""]
			}
		},

```
Notese que además de definir la longitud de cada campo, definimos el formato y particularmente definimos
que algunos campos son "tablas", dónde el dato en sí hace referencia a una tabla de valores definida también 
para que de esta forma podamos visualizar completamente la información:

```
	"sifere-jurisdicciones": {
		"901": "Capital Federal",
		"902": "Buenos Aires",
		"903": "Catamarca",
		"904": "Córdoba",
		"905": "Corrientes",
		"906": "Chaco",
		"907": "Chubut",
		"908": "Entre Ríos",
		"909": "Formosa",
		"910": "Jujuy",
		"911": "La Pampa",
		"912": "La Rioja",
		"913": "Mendoza",
		"914": "Misiones",
		"915": "Neuquén",
		"916": "Río Negro",
		"917": "Salta",
		"918": "San Juan",
		"919": "San Luis",
		"920": "Santa Cruz",
		"921": "Santa Fe",
		"922": "Santiago del Estero",
		"923": "Tierra del Fuego",
		"924": "Tucumán"
	},
	"sifere-tipo-comprobantes": {
		"F": "Factura",
		"R": "Recibo", 
		"D": "Nota de Débito",
		"C": "Nota de Crédito",
		"O": "Otro"
	},
```

De esta forma tenemos:
* Un archivo de texto con información en campos de lóngitud fija, por ejemplo: `sifere.dat`
* Una definción JSON del formato, en un archivo de nombre `parseit.fmt`
* La herramienta `parseit` o `parseit.exe`

Con esta configuración al invocar `parseit sifere.dat` obtendremos una salida como está:

```
+----------+--------------------------+--------------------------------+-------------------------+----------------------+------------------------+-----------------------+-------------------------+----------------------------------+--------------------+
|   # Reg. | Código de Jurisdicción   | CUIT del Agente de Retención   | Fecha de la Retención   |   Número de Sucursal |   Número de constancia | Tipo de Comprobante   | Letra del Comprobante   |   Número de Comprobante Original |   Importe Retenido |
|----------+--------------------------+--------------------------------+-------------------------+----------------------+------------------------+-----------------------+-------------------------+----------------------------------+--------------------|
|        1 | 901 - Capital Federal    | 30-00000000-9                  | 01-01-2006              |                 1234 |       1234567891234560 | F - Factura           | A                       |             00000000000100001235 |             125.20 |
|        2 | 901 - Capital Federal    | 30-00000000-9                  | 01-01-2006              |                 1234 |       1234567891234560 | F - Factura           | A                       |             00000000000100001235 |             125.20 |
|        3 | 901 - Capital Federal    | 30-00000000-9                  | 01-01-2006              |                 1234 |       1234567891234560 | F - Factura           | A                       |             00000000000100001235 |             125.20 |
+----------+--------------------------+--------------------------------+-------------------------+----------------------+------------------------+-----------------------+-------------------------+----------------------------------+--------------------+

```


Algunos puntos claves de este proyecto:
=======================================

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


Requerimientos e instalación:
=============================

En Windows, nada en particular ya que se distribuye la herramienta "congelada" mediante **Pyinstaller**. Descargarla y copiarla en alguna carpeta del sistema, idealmente que este apuntada al path.

* Para descargar y descomprimir **Parseit**, hacer click [aqui](https://bitbucket.org/pmoracho/python.projects/raw/bd19d803a17e2fe6720fc603117a75d2cd1c6b76/parse/dist/parseit-20160606.zip)
* El proyecto en [**Github**](https://github.com/pmoracho/parseit)


Uso:
====

```

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

Desarrollo:
===========

## Requisitos iniciales

El proyecto **parseit** esta construido usando el lenguaje **python**, a la fecha no se usan librerías adicionales a las propias de python, pero de todas formas es recomendable preparar antes que nada, un entorno de desarrollo. A continuación expondremos en detalle cuales son los pasos para tener preparado el entorno de desarrollo. Este detalle esta orientado a la implementación sobre Windows 32 bits, los pasos para versiones de 64 bits son sustancialmente distintos, en particular por algunos de los "paquetes" que se construyen a partir de módulos en C o C++, de igual forma la instalación sobre Linux tiene sus grandes diferencias. Eventualmente profundizaremos sobre estos entornos, pero en principo volvemos a señalar que el siguiente detalle aplica a los ambientes Windows de 32 bits:

* Obviamente en primer lugar necesitaremos [Python](https://www.python.org/ftp/python/3.4.0/python-3.4.0.msi), por ahora únicamente la versión 3.4. La correcta instalación se debe verificar desde la línea de comandos: `python --version`. Si todo se instaló correctamente se debe ver algo como esto `Python 3.4.0`, sino verificar que Python.exe se encuentre correctamente apuntado en el PATH.

* Es conveniente pero no mandatorio hacer upgrade de la herramienta pip: `python -m pip install --upgrade pip`

* [Virutalenv](https://virtualenv.pypa.io/en/stable/). Es la herramienta estándar para crear entornos "aislados" de python. Para no tener conflictos de desarrollo lo que haremos mediante esta herramienta es crear un "entorno virtual" de python en una carpeta del projecto (venv). Este "entorno virtual" contendrá una copia completa de Python, al activarlo se modifica el PATH al python.exe que apuntará ahora a nuestra carpeta del entorno, evitando cualquier tipo de conflicto con un entorno Python ya existente. La instalación de virtualenv se hara mediante `pip install virtualenv`

* Descargar el proyecto desde [Github](https://github.com/pmoracho/parseit), se puede descargar desde la página el proyecto como un archivo Zip, o si contamos con [Git](https://git-for-windows.github.io/) sencillamente haremos un `git clone https://github.com/pmoracho/parseit`.

* El proyecto una vez descomprimido o luego del clonado del repositorio tendrá una estructura de directorios similar a la siguiente:

```
parseit.git
   |-dist
   |-tests
   |-tools
```

## Preparación del entorno virtual local

Para poder ejecutar, o crear la distribución de la herramientas, lo primero que deberemos hacer es armar un entorno python "virtual" que alojaremos en una subcarpeta del directorio principal que llamarems "venv". En el proyecto incorporamos una herramienta de automatización de algunas tareas básicas. Se trata de `make.py`, la forma de ejecutarlo es la siguiente: `python tools\make.py <comando>` la ejecución si parámetros o mediante el parámetro `--help` arrojará una salida como lo que sigue:

```
Automatización de tareas para el proyecto Paresit
(c) 2016, Patricio Moracho <pmoracho@gmail.com>

Uso: make <command> [<args>]

Los comandos más usados:
   devcheck   Hace una verificación del entorno de desarrollo
   devinstall Realiza la instalación del entorno de desarrollo virtual e instala los requerimientos
   docinstall Intalación de Sphinx
   clear      Elimina archivos innecesarios
   test       Ejecuta todos los tests definidos del proyecto
   build      Construye la distribución binaria de las herramientas del proyecto

argumentos posicionales:
  command     Comando a ejecutar

argumentos opcionales:
  -h, --help  mostrar esta ayuda y salir
```

**Importante**: Make.py asume que se está ejecutando fuera del entorno virtual del proyecto.

Para preparar el entorno virtual simplemente haremos `python tools\make.py devinstall`, este proceso si resulta exitoso deberá haber realizado las siguientes tareas:

* Creación de un entorno pyhton virtual en la carpeta "venv", invocable mediante `venv\Scripts\activate.bat` en Windows o `source venv/Scripts/activate` en entornos Linux o Cygwin/Mingw (en Windows)
* Instalado todas las dependencias necesarias


## Notas adicionales:

* Es recomendable y cómodo, pero entiendo que no es mandatorio, contar con un entorno estilo "Linux", por ejemplo [MinGW](http://www.mingw.org/), tal como dice la página del proyecto: "MinGW provides a complete Open Source programming tool set which is suitable for the development of native MS-Windows applications, and which do not depend on any 3rd-party C-Runtime DLLs. (It does depend on a number of DLLs provided by Microsoft themselves, as components of the operating system; most notable among these is MSVCRT.DLL, the Microsoft C runtime library. Additionally, threaded applications must ship with a freely distributable thread support DLL, provided as part of MinGW itself)." De este entorno requerimos algunas herramientas de desarrollo: Bash para la línea de comandos y Make para la automatización de varias tareas del proyecto. 

* Usar "soft tabs": Con cualquier editor que usemos configurar el uso del <tab> en vez de los espacios, yo prefiero el <tab> puro al espacio, entiendo que es válido el otro criterio pero ya los fuentes están con esta configuración, por lo que para evitar problemas al compilar los .py recomiendo seguir usando este criterio. Asimismo configurar en 4 posiciones estos <tab>.


### Formatos
+ Los formatos se definen en uno o más archivos .FMT que no son más que archivos [JSON](http://www.json.org/)
+ [JSON Editor Online](http://www.jsoneditoronline.org/) Para validar la edición del archivo de formatos

Changelog:
==========

#### Version 1.1
* Primer release oficial de la herramienta
* Se distribuyen varios formatos para interpretar archivos de Afip / Siap

#### Version 0.1
* Versión inicial
