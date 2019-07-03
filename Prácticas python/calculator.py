
from colorama import Style, Fore # Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + 
import os
import time

# variables
num1 = 0
num2 = 0
num3 = 0
resultado = 0
operacion = 0
seguir = " "

def main_process():
    os.system("clear")

    # menu
    print ()
    print (Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Selecciona la operacion que deseas hacer: ")
    print ()
    print (Style.RESET_ALL + Style.BRIGHT + Fore.LIGHTBLACK_EX + "      1) SUMA         3) MULTIPLICACIÓN")
    print (Style.RESET_ALL + Style.BRIGHT + Fore.LIGHTBLACK_EX + "      2) RESTA        4) DIVISIÓN")
    print ()
    operacion = int(input (Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + "> " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
    print()
    # posibilidades:
    # suma
    if (operacion == 1):
        num1 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el primer número que quieras sumar: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        num2 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el segundo número que quieras sumar: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        seguir = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " ¿Quieres sumar más numeros? [S1/N0]: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        if (seguir == 1):
            num3 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el tercer número que quieras sumar: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
            resultado = num1 + num2 + num3
            print()
            print(f"    RESULTADO: {resultado}")
            print()
            exit()

        else:
            resultado = num1 + num2
            print()
            print(f"    RESULTADO: {resultado}")
            print()
            exit()

    # resta
    if (operacion == 2):
        num1 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el número al que quieras restar: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        num2 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el número que le quieras restar: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        resultado = num1 - num2
        print()
        print(f"    RESULTADO: {resultado}")
        print()
        exit()

    # multiplicacion
    if (operacion == 3):
        num1 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el primer número que quieras multiplicar: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        num2 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el segundo número que quieras multiplicar: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        seguir = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " ¿Quieres multiplicar más numeros? [S1/N0]: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        if (seguir == 1):
            num3 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el tercer número que quieras multiplicar: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
            resultado = num1 * num2 * num3
            print()
            print(f"    RESULTADO: {resultado}")
            print()
            exit()
        else:
            resultado = num1 * num2
            print()
            print(f"    RESULTADO: {resultado}")
            print()
            exit()

    # division
    if (operacion == 4):
        num1 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el número al que quieras dividir: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        num2 = int(input(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + " Escribe el número le que quieras dividir: " + Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE))
        resultado = num1 / num2
        print()
        print(f"    RESULTADO: {resultado}")
        print()
        exit()

    # otro
    else :
        print(Style.RESET_ALL + Style.BRIGHT + Style.DIM + Fore.WHITE + " Opcion incorrecta. [x_x] ")
        time.sleep(2)
        main_process()

main_process()
exit()