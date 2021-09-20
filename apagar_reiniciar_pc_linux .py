import os
import time

def apagar():
    os.system("shutdown -h 1")
    
def reiniciar():
    os.system("shutdown -r 1")
    
def salir():
    print('\033[5;31m' "<<<<<<<<<<Saliendo de la Herrameinta>>>>>>>>>>")
    time.sleep(5)
    exit()

def main():
    menu = '''
(1) Apagar La Computadora
(2) Reiniciar La Computadora
(3) Salir
'''
    print('\033[1;36m' + menu + '\033[1;36m')

    opcion = input("Introduzca el Numero, que corresponda a la Opcion deseada : ")

    print("\n")

    if opcion == '1':
        print('\033[5;34m' "Su Computadora se apagara en 1 minuto, introduce shutdown -c para cancelar.")
        apagar()
    elif opcion == '2':
        print('\033[5;36m' "Su Computadora se reiniciara en 1 minuto, introduce shutdown -c para cancelar.")
        reiniciar()
    elif opcion == '3':
        salir()
        
main() 