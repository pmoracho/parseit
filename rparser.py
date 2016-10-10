# -*- coding: utf-8 -*-
"""
# Copyright (c) 2014 Patricio Moracho <pmoracho@gmail.com>
#
# rparser.py
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 3 of the GNU General Public License
# as published by the Free Software Foundation. A copy of this license should
# be included in the file GPL-3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
"""
"""
	TO DO:
		+ Agregar exportación a Excel vía xlswriter
		+ Agregar injectado de css para html por parametro
		+ Problemas con FMT erroneos, no colgar y mostrar el error
		+ Proceso de archivos CSV con registros a "skipear"
		+ Mejorar la clase
        + Agregar otros atributos para la identificación de archivos, por ejem. el nombre
		+ OK. Agregar totales a la salida
		+ Ok. Mejorar e investigar el tema de los codecs. Unificar operaciones de lectura de archivo
		+ Ok. Armar funcionalidad para listar formatos uno o todos
		+ OK. Poder configurar los campos a mostrar
		+ OK. Exportar a Csv plano
		+ Ok. Vista horizontal
		+ Ok. Formatos especificos para output de campos
		+ Ok. Exportar a un archivo expecífico
		+ Ok. abrir el archivo automáticamente al finalizar
		+ Ok. Agregar variables al outputfile {tmp}, {desktop}, {rndfilename}

"""
__author__		= "Patricio Moracho <pmoracho@gmail.com>"
__appname__		= "parseit"
__appdesc__		= "Parseador de archivos"
__license__		= 'GPL v3'
__copyright__	= "2016, %s" % (__author__)
__version__		= "1.1"
__date__		= "2016/01/22 13:42:03"

try:
	import sys
	import os
	import json
	import glob
	import codecs
	import struct
	from tabulate import *
	from collections import OrderedDict
	from datetime import datetime


except ImportError as err:
	modulename = err.args[0].split()[3]
	print("No fue posible importar el modulo: %s" % modulename)
	sys.exit(-1)

class Parser(object):
	"""Parser es el motor principal para entender los archivos de registros de longitud fija.
   	"""
	def __init__(self, loadfrom, ignorefmterror=False):
		"""
		Inicialización del parser de archivos de longitud fija

		Args:
			loadform (str)			: path a uno o más archivos de definición de formatos
			ignorefmterror (bool)	: Se ignoran los errores de consistencia en cualquier .fmt?
		"""

		self._fmtfiles			= []
		self._formats			= {}
		self._tablas			= {}
		self._loadfrom			= loadfrom
		self._parsefile			= ""
		self._formatos_posibles = []
		self._records			= []
		self._parseformat		= ""
		self._parseformatname	= ""
		self._inputfile_encoding= 'utf8'
		self.dontusetables		= False
		self.addrecordnum		= True
		self.addtotals			= False
		self.openfile			= False
		self.outputfile			= None
		self.cssfile			= None
		self._load_fmt_files(ignorefmterror)
		self._add_format_info()

	def _load_fmt_files(self, ignorefmterror):
		"""Carga los archivos .fmt de definición de formatos y completa los diccionarios:

			- _fmtfiles : Lista de archivos .fmt a cargar
			- _formats 	: colección de formatos
			- _tablas	: tablas de sustitución de valores

		Args:
			ignorefmterror (bool)	: Se ignoran los errores de consistencia en cualquier .fmt?
		"""

		self._fmtfiles = glob.glob(self._loadfrom)

		if not self._fmtfiles:
			raise Exception('No se han encontrado en: {0} archivos con la definición de los formatos (FMT)'.format(self._loadfrom))

		d1 = OrderedDict()
		for f in self._fmtfiles:
			try:
				with open(f, "r", encoding='utf-8') as json_file:
					data = json.load(json_file, object_pairs_hook=OrderedDict)
					self._formats.update(data.get("formats"))
					self._tablas.update(data.get("tables"))

			except ValueError as e:
				if not ignorefmterror:
					raise Exception('{0} al intentar cargar el archivo: {1}'.format(str(e), str(f)))

	def _add_format_info(self):
		"""Agrega longitudes a cada formato,
		 generación de la estructura para paseo."""

		for k, f in self._formats.items():
			ln = 0
			s = ""
			for c in f.get("fields", {}).values():
				ln = ln + c[0]
				s = s + "{0}s".format(c[0])

			self._formats.get(k).update({"length": ln})
			self._formats.get(k).update({"struct": s})

	def _representation(self):
		r = """
			Parser(hash:{0})
			- loadfrom: {1}
			- fmtfiles: {2}
			- formatos: {3}
			- parse   : {4}
			- posibles: {5}
			""".format(self.__hash__(), self._loadfrom, self._fmtfiles, [ (key,value.get("length",0)) for key, value in self._formats.items()], self._parsefile, self._formatos_posibles)
		return r

	def __repr__(self):
		return self._representation()

	def _str_to_list(self, str, max):
		"""
		Devuelve una lista de enteros a partir de un string

			"1,2,3,4"	--> [1,2,3,4]
			"1-3,8" 	--> [1,2,3,8]

		"""
		def try_int(s):
			"""Se intenta convertir a un entero sino 0."""
			try:
				return int(s)
			except ValueError:
				return 0

		lista=[]
		if str:
			for c in str.split(","):
				if "-" in c:
					rango=c.split("-")
					for valor in range(try_int(rango[0]),try_int(rango[1])+1):
						if	valor >= 1 and valor <= max:
							lista.append(valor)
				else:
					valor = try_int(c)
					if valor >= 1 and valor <= max:
						lista.append(valor)

		return lista

	def _read_utf8ascii_file_as_uni(self, fname):
		"""Intenta leer un archivo como utf8 sino lo considera un ascii estándar."""

		try:
			self._inputfile_encoding = 'utf8'
			with codecs.open(fname,'r',encoding='utf8') as f:
				return f.read()

		except UnicodeError:

			self._inputfile_encoding = 'iso-8859-1'
			with codecs.open(fname,'r',encoding='iso-8859-1') as f:
				return f.read()

	def set_file_to_parse(self, file):
		self._parsefile = file

	def get_posible_formats(self):
		"""
		Define y devuelve los posibles formatos del archivo a procesar.

		Return:
			_formatos_posibles	lista
		"""

		self._formatos_posibles		= []
		f = self._read_utf8ascii_file_as_uni(self._parsefile)
		fln = len(f)
		rln = len(f.splitlines()[0])
		for k,f in self._formats.items():
			l = f.get("length",0)
			if l != 0:
				if rln == l:
					self._formatos_posibles.append(k)

		return self._formatos_posibles

	def parseit_as(self, format_name):

		self._parseformat		= self._formats.get(format_name)
		self._parseformatname	= format_name

		if self._parseformat is None:
			raise Exception('el formato: {0} no existe o no ha sido definido completamente. Revise el/los archivo/s *.fmt.'.format(format_name))

		tablas_fmt	= self._tablas
		estructura	= self._parseformat.get("struct")
		fields		= self._parseformat.get("fields")
		amounts = {i:v for i,(k,v) in enumerate(fields.items()) if v[1] == "amount"}
		zamounts = {i:v for i,(k,v) in enumerate(fields.items()) if v[1] == "zamount"}
		dates = {i:v for i,(k,v) in enumerate(fields.items()) if v[1] == "date"}

		if not self.dontusetables:
			tablas = { i:v for i,(k,v) in enumerate(fields.items()) if v[1] == "table"}

		with codecs.open(self._parsefile,'r',encoding=self._inputfile_encoding) as f:
			for i, l in enumerate(f.readlines(),1):

				# Parseo la linea y la combierto en un lista plana
				b = struct.unpack(estructura, l.strip().encode('iso-8859-1'))
				c = [c.decode('iso-8859-1') for c in b]

				# Conversión a datos nativos para montos
				for k,v in amounts.items():
					c[k] = float(c[k].replace(",","."))

				# Conversión a datos nativos para fechas
				for k,v in dates.items():
					if c[k].strip() != '':
						c[k] = datetime.strptime(c[k], v[2]).strftime(v[3])

				# Conversión a datos nativos para montos zero paded
				for k,v in zamounts.items():
					decimals = int(v[2])
					c[k] = float(c[k][:len(c[k])-decimals] + "." + c[k][-decimals:])

				# Reemplazo los valores de tabla
				if not self.dontusetables:
					try:
						for k,v in tablas.items():
							t = tablas_fmt.get(v[2])
							try:
								c[k] = "{0} - {1}".format( c[k], t[c[k]])
							except KeyError as e:
								c[k] = "{0} - {1}".format( c[k], "!!!error")

					except Exception:
						raise Exception('Error al al intentar procesar la tabla: {}'.format(v[2]))

				if self.addrecordnum:
					c = [i] + c

				self._records.append(c)

		# ======================
		# Arego un # de registro
		# ======================
		if self.addrecordnum:
			new_fields = fields.__class__()
			new_fields["# Reg."] = [8, "string", "", ""]
			for key, value in fields.items():
				new_fields[key]=value
			fields.clear()
			fields.update(new_fields)

	def showformats(self, nombre_formato):
		"""
		Imprime en la salida extandar la documentación de uno o todos los formatos

		Args:

			nombre_formato	: (string) nombre del formato a documentar

		"""
		if nombre_formato:
			self.showformat(nombre_formato)
		else:
			print("")
			print("=============================")
			print("Todos los formatos de parseit")
			print("=============================")
			for nf in [k for k, v in self._formats.items()]:
				self.showformat(nf)
			print("")

	def showformat(self, nombre_formato):
		"""
		Imprime en la salida extandar la documentación de un determinado formato

		Args:

			nombre_formato	: (string) nombre del formato a documentar

		"""
		formato = self._formats.get(nombre_formato, None)
		if formato:
			try:
				campos	= [(i, k, v[0], v[1], v[2], v[3]) for i,(k,v) in enumerate(formato.get("fields").items(),1)]
				header	= ["#", "Nombre del campo", "Longitud", "Tipo", "info adicional", "formato salida"]
				ln		= sum([ln for i, nom, ln, tipo, info, salida in campos])

				print("\nFormato   : {1}\nCategoria : {0}\nLongitud  : {2}\n".format(formato.get("category","n/d"),nombre_formato,ln))
				print(tabulate(	tabular_data	= campos,
								headers			= header,
								floatfmt		= "g",
								tablefmt		= 'psql',
								numalign		= "right",
								stralign		= "left"))

			except Exception:
				print("Error al procesar el formato: \"{0}\". Revise la configuración dek mismo.".format(nombre_formato))
		else:
			print("No se encontró el formato \"{0}\"".format(nombre_formato))


	def export(self, export_format, showcols=None, showrows=None, horizontalmode=False):
		"""
		Exportación del archivo interpretado según  el format especificado

		Args:

			export_format	: (string) nombre del formato a utilizar
			showcols		: (string) columnas a mostrar
			showrows		: (string) filas a mostrar
			horizontalmode	: (bool) Display de la tabla en formato horizontal, las columnas se muestran como registros


		"""

		nombrecampos		= [k for k, v in self._parseformat.get("fields").items()]
		propiedades			= [v for k, v in self._parseformat.get("fields").items()]
		campos_a_mostrar 	= None
		filas_a_mostrar 	= None

		if showrows:
			filas_a_mostrar = self._str_to_list(showrows, len(self._records))

		if showcols:
			campos_a_mostrar = self._str_to_list(showcols, len(self._parseformat.get("fields")))
		else:
			campos_a_mostrar = [i for i, e in enumerate(self._parseformat.get("fields"), 1)]

		registros = []
		if filas_a_mostrar:
			for r in self._records:
				if r[0] in filas_a_mostrar:
					registros.append([r[c-1] for c in campos_a_mostrar])
		else:
			if showcols:
				for r in self._records:
					registros.append([r[c-1] for c in campos_a_mostrar])
			else:
				registros = self._records

		real_rows			= len(registros)
		header_row			= [nombrecampos[c-1] for c in campos_a_mostrar]
		fields_props		= [propiedades[c-1] for c in campos_a_mostrar]
		override_cols_fmt	= [p[3] if p[3] else None for p in fields_props]

		# Sumarizar campos
		if self.addtotals:
			scampos = [i for i, c in enumerate(registros[0], 0) if (isinstance(c, int) or isinstance(c, float)) and i != 0]
			totales = [0 for c in campos_a_mostrar]
			for r in registros:
				for s in scampos:
					totales[s] = totales[s] + r[s]

			for i, e in enumerate(totales, 0):
				if i not in scampos:
					totales[i] = None

			registros.append(totales)

		if export_format == "csv":
			numalign = None
			stralign = None
		else:
			numalign = "right"
			stralign = "left"

		if horizontalmode:
			filas = []
			maxlen = len(max(header_row, key=len))
			for r in registros:
				for i, h in enumerate(header_row, 0):
					filas.append([h, r[i]])
					l = len(max([str(c) for c in r], key=len))
					if maxlen < l:
						maxlen = l

				filas.append(["-"*maxlen, "-"*maxlen])

			header_row = ["Campo", "Valor"]
			override_cols_align = ["right", "left"]
			registros = filas
		else:
			override_cols_align = None


		tablestr = tabulate(tabular_data		= registros,
							headers				= header_row,
							floatfmt			= "8.2f",
							tablefmt			= export_format,
							numalign			= numalign,
							stralign			= stralign,
							override_cols_align = override_cols_align,
							override_cols_fmt	= override_cols_fmt
							)

		if export_format == "html":
			css_default = """
			table.tabulate {
				font-family: Verdana, Geneva, sans-serif;
				font-size:10px;
				color:#000000;
				border-width: 1px;
				border-color: #eeeeee;
				border-collapse: collapse;
				background-color: #ffffff;
				width: 100%;
				table-layout: auto;
			}
			table.tabulate th {
				border-width: 1px;
				padding: 1px;
				border-style: solid;
				border-color: #eeeeee;
				background-color: #004f6f;
				color:#fff;
				text-align: left;
			}
			table.tabulate td {
				border-width   : 1px;
				padding		   : 1px;
				border-style   : solid;
				border-color   : #eeeeee;
				vertical-align : top;
			}
			table.tabulate tr:nth-of-type(even) {
				background-color:#D2E4FC;
			}
			table.tabulate tr:nth-of-type(odd) {
				background-color:#F7FDFA;
			}
			p {
				font-family: Verdana, Geneva, sans-serif;
				font-size:14px;
				width: 100%;
				padding: 0px;
				margin: 0px;
				text-align: center;
			}
			"""

			if self.cssfile != None:
				css = self._read_utf8ascii_file_as_uni(self.cssfile)
			else:
				css = css_default

			title		= 	'Archivo: {0} ({1})'.format(self._parsefile,self._parseformatname)
			cantrows	= 	'Cantidad de registros visualizados: {0}'.format(real_rows)
			tablestr 	=	'<!doctype html>\n' \
							'<html lang="en">\n' \
							'<head>\n' \
							'<meta charset="utf-8">\n' \
							'<meta name="description" content="' + __appname__ + ' - ' + __appdesc__ + '">\n' \
							'<meta name="author" content="' + __copyright__ + '">\n' \
							'<style type="text/css">\n{0}\n</style>\n<title>{1}</title>\n</head>\n<body>\n'.format(css,title) + \
							'<p><b>' + title + '</b></p>' + \
							'<p>' + cantrows + '</p>' + \
							'<p></br></p>' + \
							tablestr + '</body>\n</html>\n'

		if self.outputfile:
			with open(self.outputfile, "w") as out:
				print(tablestr, file=out)
				if self.openfile:
					try:
						os.startfile(self.outputfile)
					except FileNotFoundError as e:
						print(u"Ocurrio el error %s al intentar abrir el archivo '%s'" % (str(e), filename))
		else:
			print(tablestr)
