import sys
#revisar el OS en que corre el script
import os
if sys.platform=="linux2":
	os.system('clear')
	print "la plataforma es linux"
else:
	os.system('cls')
	print "la plataforma es",sys.platform
