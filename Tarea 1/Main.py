from Cadena import *
from Log import *
    
def main():
    logger = inicio_logger()
    logger.info("comienza el programa")

    print("Inicio de programa")
    print("Presione enter para terminar")
    
    while(True):
        it=1
        data = input("Ingrese cadena: ")
        if(data != ""):
            cadena = Cadena(data)
            if(cadena.validar()):
                logger.error("Entrada "+str(it)+": "+cadena.name()+" inválida")
                print("Valor no válido")
                pass
            else:
                cadena_comprimida = cadena.comprimir()
                if (len(cadena.name()) < len(cadena_comprimida)):
                    cadena_comprimida = cadena.name()
                logger.info("Entrada "+str(it)+": "+cadena.name()+" válida. Valor obtenido: "+cadena_comprimida)
                print(cadena_comprimida)
            it+=1
        else:
            print("adios")
            break
    logger.info("Fin ejecución")
main()
    
