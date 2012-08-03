#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse, sys, os

if sys.platform.startswith('linux'):
	os.system('clear')
	print "la plataforma es linux"
elif sys.platform.startswith('win'): 
	os.system('cls')
	print "la plataforma es windows"

def extractpuke(fich):
	"Extrae un archivo puke"
	if os.path.isfile(fich):
		try:
			import zipfile
			if zipfile.is_zipfile(fich):
				print "Procesando archivo puke..."
				zip=zipfile.ZipFile(fich,"r")
				print "Listando informacion del archivo"
				print 
				print zip.printdir()
				print 
				print "Extrayendo el archivo",fich, "a puke/"
				zip.extractall("puke")
				zip.close()
			else:
				print "El archivo",fich,"no es un archivo puke valido o esta dañado"
		except:
			print "Ocurrio un error al procesar el archivo",fich
	else:
		print fich,"El archivo no existe en la ruta especificada"

def listpuke(fich):
	"Listar el contenido de un archivo puke"
	pass

parser = argparse.ArgumentParser(usage='%(prog)s [opciones]')
parser.add_argument("-e", help="Extrae un fichero .puke",type=extractpuke)
parser.add_argument("-l", help="Lista un fichero .puke",type=listpuke)
parser.add_argument("-v", help="Muestra la version actual de pukecli", 
					action='version',version='%(prog)s 0.2')
args = parser.parse_args()
