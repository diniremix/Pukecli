#! /usr/bin/env python
import argparse
import os
os.system('cls')

parser = argparse.ArgumentParser(usage='%(prog)s [opciones]')
parser.add_argument("-e", help="Extrae un fichero .puke",type=extractpuke)
parser.add_argument("-c", help="Crea un fichero .puke",type=createpuke)
parser.add_argument("-v", help="Muestra la version actual de pukecli", 
					action='version',version='%(prog)s 0.2')
args = parser.parse_args()
