# -*- coding: utf-8 -*-

"""
# Copyright (c) 2014 Patricio Moracho <pmoracho@gmail.com>
#
# parseit
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

__author__		= "Patricio Moracho <pmoracho@gmail.com>"
__appname__		= "parseit"
__appdesc__		= "Parseador de archivos"
__license__		= 'GPL v3'
__copyright__	= "2016, %s" % (__author__)
__version__		= "1.1"
__date__		= "2016/01/22 13:42:03"

"""
###############################################################################
# Imports
###############################################################################
"""
try:
	import os
	import sys
	import gettext
	import tempfile
	from rparser import Parser

	"""
	Librerias adicionales
	"""

	def my_gettext(s):
		"""my_gettext: Traducir algunas cadenas de argparse."""
		current_dict = {'usage: ': 'uso: ',
						'optional arguments': 'argumentos opcionales',
						'show this help message and exit': 'mostrar esta ayuda y salir',
						'positional arguments': 'argumentos posicionales',
						'the following arguments are required: %s': 'los siguientes argumentos son requeridos: %s'}

		if s in current_dict:
			return current_dict[s]
		return s

	gettext.gettext = my_gettext

	import argparse
	from argparse import RawTextHelpFormatter

except ImportError as err:
	modulename = err.args[0].split()[3]
	print("No fue posible importar el modulo: %s" % modulename)
	sys.exit(-1)


##################################################################################################################################################
## Inicializar parametros del programa
##################################################################################################################################################
def init_argparse():

	usage			= 	'\nEjemplos de uso:\n\n' \
						'- Interpretar un archivo infiriendo el formato:\n' \
						'  %(prog)s [opciones] <archivo a interpretar>\n\n' \
						'- Mostrar todos los formatos disponibles y sus definiciones:\n' \
						'  %(prog)s [opciones] -s [opciones]\n\n' \
						'- Mostrar esta ayuda:\n' \
						'  %(prog)s -h\n\n' 


	cmdparser = argparse.ArgumentParser(prog			= __appname__, 
										description		= "%s\n%s\n" % (__appdesc__,__copyright__ ), 
										epilog			= usage,
										formatter_class = lambda prog: argparse.RawTextHelpFormatter(prog,max_help_position=35), 
										usage			= None
										)

	cmdparser.add_argument('inputfile'			, type=str, nargs='?', help="Archivo de input", metavar="\"archivo a interpretar\"")	

	cmdparser.add_argument("-v", "--version"	    		, action='version', version=__version__)							
	cmdparser.add_argument('-f', '--format'		, type=str	, action="store", dest="formato", help="Definir path o archivo FMT a utilizar", metavar="\"path o archivo\"")	
	cmdparser.add_argument('-u', '--useformat'	, type=str	, action="store", dest="useformat", help="Forzar el uso de un determinado formato para porcesar el archivo", metavar="\"formato\"")	
	cmdparser.add_argument('-t', '--dontusetables'			, action="store_true", dest="dontusetables", help="No usar traducción por tablas y mostrar los datos nativos")	
	cmdparser.add_argument('-s', '--showformat'		    	, action="store_true", dest="showformat", help="Mostrar información de un formato (--format) en particular o todos los definidos")	
	cmdparser.add_argument('-i', '--ignorefmterror'			, action="store_true", dest="ignorefmterror", help="Ignorar errores al cargar archivos de formatos")	
	cmdparser.add_argument('-o', '--outputfile'			    , action="store", dest="outputfile", help="Exportar a un archivo", metavar="\"archivo\"")	
	cmdparser.add_argument('-x', '--openfile'			    , action="store_true", dest="openfile", help="abrir automáticamente el archivo")	
	cmdparser.add_argument('-e', '--exportformat'			, action="store", dest="exportformat", help="Exportar en un formato específico", metavar="\"formato\"", default="psql")	
	cmdparser.add_argument('-c', '--showcols', type=str		, action="store", dest="showcols", help=u"Números de las columnas a mostrar", metavar="\"columnas\"")	
	cmdparser.add_argument('-r', '--showrows', type=str		, action="store", dest="showrows", help=u"Números de las filas a mostrar", metavar="\"filas\"")	
	cmdparser.add_argument('-n', '--dontshowrecordnumber'	, action="store_false", dest="addrecordnumber", help="No mostrar los números de cada registro")	
	cmdparser.add_argument('-z', '--horizontalmode'			, action="store_true", dest="horizontalmode", help="Modo de visualización horizontal")	
	cmdparser.add_argument('-a', '--addtotals'			    , action="store_true", dest="addtotals", help="Agregar una última fila con los totales de los campos númericos")	
	cmdparser.add_argument('-l', '--css-file'			    , action="store", dest="cssfile", help="Archivo de estilos (.Css) para la salida Html", metavar="\"archivo css\"")
	
	return cmdparser

def showerror(msg):
	print("\n!!!! %s error: %s\n" % (__appname__, msg) )


def resource_path(relative):
	"""Obtiene un path, toma en consideración el uso de pyinstaller"""
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)


def expand_filename(filename):

	if '{desktop}' in filename:
		print(filename)
		tmp = os.path.join(os.path.expanduser('~'), 'Desktop')
		print(tmp)
		filename = filename.replace('{desktop}', tmp)

	if '{tmpdir}' in filename:
		tmp = tempfile.gettempdir()
		filename = filename.replace('{tmpdir}', tmp)

	if '{tmpfile}' in filename:
		tmp = tempfile.mktemp()
		filename = filename.replace('{tmpfile}', tmp)

	return filename

"""
##################################################################################################################################################
# Main program
##################################################################################################################################################
"""
if __name__ == "__main__":

	cmdparser = init_argparse()
	try:
		args = cmdparser.parse_args()
	except IOError as msg:
		cmdparser.error(str(msg))
		sys.exit(-1)

	"""
	O se muestran los formatos o se procesa un archivo
	"""
	if not args.showformat and not args.inputfile:
		cmdparser.error("Se debe indicar alguna opción válida -s/--showformat o \"archivo a interpretar\"\n")
		sys.exit(-1)

	# Definir el path de dónde obtener la configuración
	if not args.formato:
		# determine if application is a script file or frozen exe
		if getattr(sys, 'frozen', False):
			application_path = os.path.dirname(sys.executable)
		elif __file__:
			application_path = os.path.dirname(__file__)
		
		# print("basedir : {0}".format(application_path))

		default_fmt_file = 'parseit.fmt'
		fmtpath = resource_path(os.path.join(application_path, default_fmt_file))
	else:
		fmtpath = args.formato

	try:
		parser = Parser(fmtpath, args.ignorefmterror)

	except Exception as e:
		showerror(e)
		sys.exit(-1)

	if args.showformat:
		parser.showformats(args.useformat)
		sys.exit(0)

	if args.inputfile:
		parser.set_file_to_parse(args.inputfile)

		try:
			posibles = parser.get_posible_formats()
		except Exception as e:
			showerror(e)
			sys.exit(-1)

		if len(posibles) == 1:
			formato = posibles[0]
		else:
			if not args.useformat:
				showerror("Debe seleccionar el formato del archivo ya que no ha sido posible identificarlo. Los posibles formatos son: {0}\n".format(posibles))
				cmdparser.print_help()
				sys.exit(-1)
			else:
				formato = args.useformat

		"""
		Parseo finalmente el archivo
		"""
		try:
			parser.dontusetables	= args.dontusetables
			parser.addrecordnumber	= args.addrecordnumber
			parser.addtotals		= args.addtotals
			parser.cssfile			= args.cssfile
			parser.openfile         = args.openfile

			if args.outputfile:
				parser.outputfile	= expand_filename(args.outputfile)

			parser.parseit_as(formato)
			parser.export(args.exportformat, args.showcols, args.showrows, args.horizontalmode)
		except Exception as e:
			showerror(e)
			sys.exit(-1)

	sys.exit(0)
