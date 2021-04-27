class Cadena:
    def __init__(self, cadena):
        self.__cadena=cadena

    def name(self):
        return self.__cadena
    
    #Verifica que la cadena no contenga números
    def validar(self):
        r = [False, ""]
        if len(self.__cadena)> 150:
            r = [True, "Largo de la cadena excede el largo válido (150 caracteres)"]
        elif any(char.isdigit() for char in self.__cadena):
            r = [True, "Cadena con caracteres numéricos"]
        elif self.__cadena == "":
            r = [True, "Cadena vacía"]
        return r

    #Comprime la cadena
    def comprimir(self):
        final_string = self.__cadena[0]
        aux = 1
        for i in range(1,len(self.__cadena)):
            if (self.__cadena[i-1] == self.__cadena[i]):
                aux+=1
            else:
                final_string = final_string + str(aux) + self.__cadena[i]
                aux = 1
        return final_string + str(aux)
