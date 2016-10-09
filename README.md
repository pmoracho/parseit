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
* El proyecto en [**Github**](https://github.com/pmoracho/parseit)


### Uso:

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

### Formatos
+ Los formatos se definen en uno o más archivos .FMT que no son más que archivos [JSON](http://www.json.org/)
+ [JSON Editor Online](http://www.jsoneditoronline.org/) Para validar la edición del archivo de formatos


### Changelog:

#### Version 1.1
* Primer release oficial de la herramienta
* Se distribuyen varios formatos para interpretar archivos de Afip / Siap

#### Version 0.1
* Versión inicial
