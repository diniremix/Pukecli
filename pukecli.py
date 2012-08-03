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
	pass

parser = argparse.ArgumentParser(usage='%(prog)s [opciones]')
parser.add_argument("-e", help="Extrae un fichero .puke",type=extractpuke)
parser.add_argument("-v", help="Muestra la version actual de pukecli", 
					action='version',version='%(prog)s 0.2')
args = parser.parse_args()
