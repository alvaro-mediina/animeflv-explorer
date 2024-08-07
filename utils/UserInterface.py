from utils import Prints
from utils import Queries

#Printeo menú y selecciono la opción
def init():
    Prints.print_menu()
    config = (input("Seleccione opción -> "))

    if(config == '1'):
        query = input("\nNombre del anime: ")
        Prints.print_titles(query)
    else:
        exit()