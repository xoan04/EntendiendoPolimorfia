def ingresarCad (cad):
    cad.ingresar()
def verificarAlfabeto(cadAlfabeto):
    cadAlfabetoToSet = set(cadAlfabeto)
    new_list = list(cadAlfabetoToSet)
    return new_list
    
class Alfabeto:    

    def __init__(self, cadena):
        self.cadAlfabeto = cadena
        

    def __repr__(self):
        return str(self.cadAlfabeto)

    def ingresar(self,cadAlfabeto):
        cadAlfabeto = verificarAlfabeto(cadAlfabeto)
        

class Lenguaje:
    def __init__(self, cadenaL):
        self.cadLenguage = cadena
        

    def __repr__(self):
        return str(self.cadLenguage)

main_list = [""]
Lista_Union=[]
resultantList = []
cantidadAlfb = int( input("Ingrese la cantidad de alfabetos que desea: "))

    for i in range (cantidadAlfb):
        cadAlfabeto = input("ingrese su cadena número "+str(i+1)+" separada por espacios: ").split(" ")
        ingresar(cadAlfabeto)
        objeto=Alfabeto(cadAlfabeto)
        main_list.append(objeto)
        ingresar(cadAlfabeto)
