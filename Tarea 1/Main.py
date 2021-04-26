#!/usr/bin/env python

import time
from Cadena import *
from Log import *

from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    # Handle any cleanup here
    print('Hasta la próxima')
    time.sleep(1)
    exit(0)

def main():
    logger = inicio_logger()
    logger.info("comienza el programa")

    print("Inicio de programa")
    time.sleep(1)
    print("ctrl+c para finalizar")
    time.sleep(1)
    while(True):
        it=1
        data = input("Ingrese cadena: ")
        signal(SIGINT, handler)
        cadena = Cadena(data)
        valor, error = cadena.validar()
        if(valor):
            logger.error("Entrada "+str(it)+": "+cadena.name()+" inválida "+error)
            print("Error, cadena inválida. "+error)
            pass
        else:
            cadena_comprimida = cadena.comprimir()
            if (len(cadena.name()) < len(cadena_comprimida)):
                cadena_comprimida = cadena.name()
            logger.info("Entrada "+str(it)+": "+cadena.name()+" válida. Valor obtenido: "+cadena_comprimida)
            print(cadena_comprimida)
        it+=1
    logger.info("Fin ejecución")

main()
