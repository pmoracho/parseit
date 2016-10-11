Parseit
=======

`Parseit` es una herramienta de linea de comandos para "interpretar" archivos de texto con formato. 

Para entender que es `parseit` nada mejor que un ejemplo pr�ctico. Para el intercambio de informaci�n con el Afip, se 
suele trabajar con este tipo de archivos, en particular los contribuyentes grandes, que suelen generar gran cantidad
de informaci�n, veamos un caso t�pico, el Sistema federal de informaci�n m�s conocido domo **SIFERE** permite
importar masivamente la informaci�n de retenciones y percepciones, la informaci�n se arma en archivos de texto, 
con campos de l�ngitud fija y caracteres de fin de linea:

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
				"C�digo de Jurisdicci�n" : 													[ 3, "table", "sifere-jurisdicciones", ""],
				"CUIT del Agente de Retenci�n" : 											[13, "string", "", ""],
				"Fecha de la Retenci�n" : 													[10, "date", "%d/%m/%Y", "%d-%m-%Y"],
				"N�mero de Sucursal" :	 													[ 4, "string", "", ""],
				"N�mero de constancia" :													[16, "string", "", ""],
				"Tipo de Comprobante" :														[ 1, "table", "sifere-tipo-comprobantes", ""],
				"Letra del Comprobante" :													[ 1, "string", "", ""],
				"N�mero de Comprobante Original" :											[20, "string", "", ""],
				"Importe Retenido" :														[11, "amount", "", ""]
			}
		},

```
Notese que adem�s de definir la longitud de cada campo, definimos el formato y particularmente definimos
que algunos campos son "tablas", d�nde el dato en s� hace referencia a una tabla de valores definida tambi�n 
para que de esta forma podamos visualizar completamente la informaci�n:

```
	"sifere-jurisdicciones": {
		"901": "Capital Federal",
		"902": "Buenos Aires",
		"903": "Catamarca",
		"904": "C�rdoba",
		"905": "Corrientes",
		"906": "Chaco",
		"907": "Chubut",
		"908": "Entre R�os",
		"909": "Formosa",
		"910": "Jujuy",
		"911": "La Pampa",
		"912": "La Rioja",
		"913": "Mendoza",
		"914": "Misiones",
		"915": "Neuqu�n",
		"916": "R�o Negro",
		"917": "Salta",
		"918": "San Juan",
		"919": "San Luis",
		"920": "Santa Cruz",
		"921": "Santa Fe",
		"922": "Santiago del Estero",
		"923": "Tierra del Fuego",
		"924": "Tucum�n"
	},
	"sifere-tipo-comprobantes": {
		"F": "Factura",
		"R": "Recibo", 
		"D": "Nota de D�bito",
		"C": "Nota de Cr�dito",
		"O": "Otro"
	},
```

De esta forma tenemos:
* Un archivo de texto con informaci�n en campos de l�ngitud fija, por ejemplo: `sifere.dat`
* Una definci�n JSON del formato, en un archivo de nombre `parseit.fmt`
* La herramienta `parseit` o `parseit.exe`

Con esta configuraci�n al invocar `parseit sifere.dat` obtendremos una salida como est�:

```
+----------+--------------------------+--------------------------------+-------------------------+----------------------+------------------------+-----------------------+-------------------------+----------------------------------+--------------------+
|   # Reg. | C�digo de Jurisdicci�n   | CUIT del Agente de Retenci�n   | Fecha de la Retenci�n   |   N�mero de Sucursal |   N�mero de constancia | Tipo de Comprobante   | Letra del Comprobante   |   N�mero de Comprobante Original |   Importe Retenido |
|----------+--------------------------+--------------------------------+-------------------------+----------------------+------------------------+-----------------------+-------------------------+----------------------------------+--------------------|
|        1 | 901 - Capital Federal    | 30-00000000-9                  | 01-01-2006              |                 1234 |       1234567891234560 | F - Factura           | A                       |             00000000000100001235 |             125.20 |
|        2 | 901 - Capital Federal    | 30-00000000-9                  | 01-01-2006              |                 1234 |       1234567891234560 | F - Factura           | A                       |             00000000000100001235 |             125.20 |
|        3 | 901 - Capital Federal    | 30-00000000-9                  | 01-01-2006              |                 1234 |       1234567891234560 | F - Factura           | A                       |             00000000000100001235 |             125.20 |
+----------+--------------------------+--------------------------------+-------------------------+----------------------+------------------------+-----------------------+-------------------------+----------------------------------+--------------------+

```


Algunos puntos claves de este proyecto:
=======================================

* Herramienta de l�nea de comandos
* Interpretaci�n de archivos de texto de formato especifico, con caracter de fin de l�nea. M�s adelante veremos como manejar otros formatos.
* Uso de archivos JSON para la definici�n del formato (consultar parseit.json)
	* Definic�n de campos, longitudes y formatos varios
	* Definci�n de valores tipo tabla (codigo: valor) para reemplazo al mostrar de los mismos
* Especificaci�n de un formato determinado o por defecto el archivo "parseit.fmt" que estuviera en la misma carpeta de ejecutable
* Varios formatos de exportaci�n de los datos, entre otros:
	* psql 
	* csv
	* html
	* etc.
* Definir que filas y que columnas mostrar
* �til visualizaci�n o "transposici�n" de la tabla al modo "horizontal"
* Poder incorporar un hoja de estilos cuando los datos los mostramos en html
* Poder exportar a un archivo determinado y apertura autom�tica del mismo
* Con la distribuci�n se distribuyen los formatos para interpretar los archivos de texto para el Siap / Afip:
	* **ARCIBA**: debitos y cr�ditos
	* **RG3685**: Compras: comprobantes y alicuotas, Ventas: comprobantes y alicuotas
	* **SIFERE**: Retenciones y percepciones
	* **SICORE**: Retenciones y percepciones


Requerimientos e instalaci�n:
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
  -t, --dontusetables              No usar traducci�n por tablas y mostrar los datos nativos
  -s, --showformat                 Mostrar informaci�n de un formato (--format) en particular o todos los definidos
  -i, --ignorefmterror             Ignorar errores al cargar archivos de formatos
  -o "archivo", --outputfile "archivo"
                                   Exportar a un archivo
  -x, --openfile                   abrir autom�ticamente el archivo
  -e "formato", --exportformat "formato"
                                   Exportar en un formato espec�fico
  -c "columnas", --showcols "columnas"
                                   N�meros de las columnas a mostrar
  -r "filas", --showrows "filas"   N�meros de las filas a mostrar
  -n, --dontshowrecordnumber       No mostrar los n�meros de cada registro
  -z, --horizontalmode             Modo de visualizaci�n horizontal
  -a, --addtotals                  Agregar una �ltima fila con los totales de los campos n�mericos
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

El proyecto **parseit** esta construido usando el lenguaje **python**, a la fecha no se usan librer�as adicionales a las propias de python, pero de todas formas es recomendable preparar antes que nada, un entorno de desarrollo. A continuaci�n expondremos en detalle cuales son los pasos para tener preparado el entorno de desarrollo. Este detalle esta orientado a la implementaci�n sobre Windows 32 bits, los pasos para versiones de 64 bits son sustancialmente distintos, en particular por algunos de los "paquetes" que se construyen a partir de m�dulos en C o C++, de igual forma la instalaci�n sobre Linux tiene sus grandes diferencias. Eventualmente profundizaremos sobre estos entornos, pero en principo volvemos a se�alar que el siguiente detalle aplica a los ambientes Windows de 32 bits:

* Obviamente en primer lugar necesitaremos [Python](https://www.python.org/ftp/python/3.4.0/python-3.4.0.msi), por ahora �nicamente la versi�n 3.4. La correcta instalaci�n se debe verificar desde la l�nea de comandos: `python --version`. Si todo se instal� correctamente se debe ver algo como esto `Python 3.4.0`, sino verificar que Python.exe se encuentre correctamente apuntado en el PATH.

* Es conveniente pero no mandatorio hacer upgrade de la herramienta pip: `python -m pip install --upgrade pip`

* [Virutalenv](https://virtualenv.pypa.io/en/stable/). Es la herramienta est�ndar para crear entornos "aislados" de python. Para no tener conflictos de desarrollo lo que haremos mediante esta herramienta es crear un "entorno virtual" de python en una carpeta del projecto (venv). Este "entorno virtual" contendr� una copia completa de Python, al activarlo se modifica el PATH al python.exe que apuntar� ahora a nuestra carpeta del entorno, evitando cualquier tipo de conflicto con un entorno Python ya existente. La instalaci�n de virtualenv se hara mediante `pip install virtualenv`

* Descargar el proyecto desde [Github](https://github.com/pmoracho/parseit), se puede descargar desde la p�gina el proyecto como un archivo Zip, o si contamos con [Git](https://git-for-windows.github.io/) sencillamente haremos un `git clone https://github.com/pmoracho/parseit`.

* El proyecto una vez descomprimido o luego del clonado del repositorio tendr� una estructura de directorios similar a la siguiente:

```
parseit.git
   |-dist
   |-tests
   |-tools
```

## Preparaci�n del entorno virtual local

Para poder ejecutar, o crear la distribuci�n de la herramientas, lo primero que deberemos hacer es armar un entorno python "virtual" que alojaremos en una subcarpeta del directorio principal que llamarems "venv". En el proyecto incorporamos una herramienta de automatizaci�n de algunas tareas b�sicas. Se trata de `make.py`, la forma de ejecutarlo es la siguiente: `python tools\make.py <comando>` la ejecuci�n si par�metros o mediante el par�metro `--help` arrojar� una salida como lo que sigue:

```
Automatizaci�n de tareas para el proyecto Paresit
(c) 2016, Patricio Moracho <pmoracho@gmail.com>

Uso: make <command> [<args>]

Los comandos m�s usados:
   devcheck   Hace una verificaci�n del entorno de desarrollo
   devinstall Realiza la instalaci�n del entorno de desarrollo virtual e instala los requerimientos
   docinstall Intalaci�n de Sphinx
   clear      Elimina archivos innecesarios
   test       Ejecuta todos los tests definidos del proyecto
   build      Construye la distribuci�n binaria de las herramientas del proyecto

argumentos posicionales:
  command     Comando a ejecutar

argumentos opcionales:
  -h, --help  mostrar esta ayuda y salir
```

**Importante**: Make.py asume que se est� ejecutando fuera del entorno virtual del proyecto.

Para preparar el entorno virtual simplemente haremos `python tools\make.py devinstall`, este proceso si resulta exitoso deber� haber realizado las siguientes tareas:

* Creaci�n de un entorno pyhton virtual en la carpeta "venv", invocable mediante `venv\Scripts\activate.bat` en Windows o `source venv/Scripts/activate` en entornos Linux o Cygwin/Mingw (en Windows)
* Instalado todas las dependencias necesarias


## Notas adicionales:

* Es recomendable y c�modo, pero entiendo que no es mandatorio, contar con un entorno estilo "Linux", por ejemplo [MinGW](http://www.mingw.org/), tal como dice la p�gina del proyecto: "MinGW provides a complete Open Source programming tool set which is suitable for the development of native MS-Windows applications, and which do not depend on any 3rd-party C-Runtime DLLs. (It does depend on a number of DLLs provided by Microsoft themselves, as components of the operating system; most notable among these is MSVCRT.DLL, the Microsoft C runtime library. Additionally, threaded applications must ship with a freely distributable thread support DLL, provided as part of MinGW itself)." De este entorno requerimos algunas herramientas de desarrollo: Bash para la l�nea de comandos y Make para la automatizaci�n de varias tareas del proyecto. 

* Usar "soft tabs": Con cualquier editor que usemos configurar el uso del <tab> en vez de los espacios, yo prefiero el <tab> puro al espacio, entiendo que es v�lido el otro criterio pero ya los fuentes est�n con esta configuraci�n, por lo que para evitar problemas al compilar los .py recomiendo seguir usando este criterio. Asimismo configurar en 4 posiciones estos <tab>.


### Formatos
+ Los formatos se definen en uno o m�s archivos .FMT que no son m�s que archivos [JSON](http://www.json.org/)
+ [JSON Editor Online](http://www.jsoneditoronline.org/) Para validar la edici�n del archivo de formatos

Changelog:
==========

#### Version 1.1
* Primer release oficial de la herramienta
* Se distribuyen varios formatos para interpretar archivos de Afip / Siap

#### Version 0.1
* Versi�n inicial
