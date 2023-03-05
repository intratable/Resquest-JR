import subprocess
import time

dni= 0

fin=10000

def bucle():
    subprocess.call(['python','checkapi.py',str(dni)])

while dni<=fin:
    bucle()   
    print(str(dni)+' - OK') 
    dni = int(dni)
    dni =dni+1