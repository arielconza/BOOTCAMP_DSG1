import os
import tabulate
import time
from librerias.lib_empresas import *

# Cargar datos desde el archivo
f = open('empresas.txt', 'r')
str_empresas = f.read()
f.close()

# Cargar datos en la lista
lista_empresas = cargar_datos(str_empresas)

ANCHO = 50
opcion = 0

while opcion < 5:
    os.system("clear")  # Limpiar la pantalla
    mostrar_menu(ANCHO)  # Mostrar el menú
    opcion = int(input("INGRESE OPCIÓN: "))  # Leer opción del usuario
    os.system("clear")  # Limpiar la pantalla después de la opción

    if opcion == 1:
        print("="*ANCHO)
        print(" "*10 + "[1] REGISTRAR EMPRESA")
        print("="*ANCHO)
        ruc = input("RUC: ")
        razon_social = input("RAZÓN SOCIAL: ")
        direccion = input("DIRECCIÓN: ")
        dic_nueva_empresa = {
            'ruc': ruc,
            'razon_social': razon_social,
            'direccion': direccion
        }
        lista_empresas.append(dic_nueva_empresa)
        print("EMPRESA REGISTRADA CON ÉXITO")

    elif opcion == 2:
        print("="*ANCHO)
        print(" "*10 + "[2] MOSTRAR EMPRESAS")
        print("="*ANCHO)
        cabeceras = ["RUC", "RAZÓN SOCIAL", "DIRECCIÓN"]
        tabla = [empresa.values() for empresa in lista_empresas]
        print(tabulate.tabulate(tabla, headers=cabeceras, tablefmt="grid"))
        input("Presione ENTER para continuar...")

    elif opcion == 3:
        print("="*ANCHO)
        print(" "*10 + "[3] ACTUALIZAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RUC DE LA EMPRESA A ACTUALIZAR: ')
        posicion_busqueda = buscar_empresa(valor_busqueda, lista_empresas)

        if posicion_busqueda == -1:
            print("NO SE ENCONTRÓ LA EMPRESA SOLICITADA")
        else:
            print(f'EMPRESA A ACTUALIZAR: {lista_empresas[posicion_busqueda].get("razon_social")}')
            nuevo_ruc = input("NUEVO RUC: ")
            nueva_razon_social = input("NUEVA RAZÓN SOCIAL: ")
            nueva_direccion = input("NUEVA DIRECCIÓN: ")
            dic_actualizar_empresa = {
                'ruc': nuevo_ruc,
                'razon_social': nueva_razon_social,
                'direccion': nueva_direccion
            }
            lista_empresas[posicion_busqueda] = dic_actualizar_empresa
            print("EMPRESA ACTUALIZADA CON ÉXITO")

    elif opcion == 4:
        print("="*ANCHO)
        print(" "*10 + "[4] ELIMINAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RUC DE LA EMPRESA A ELIMINAR: ')
        posicion_busqueda = buscar_empresa(valor_busqueda, lista_empresas)

        if posicion_busqueda == -1:
            print("NO SE ENCONTRÓ LA EMPRESA SOLICITADA")
        else:
            lista_empresas.pop(posicion_busqueda)
            print("EMPRESA ELIMINADA CON ÉXITO")

    elif opcion == 5:
        print("="*ANCHO)
        print(" "*10 + "[5] SALIR")
        str_empresas = grabar_datos(lista_empresas)
        with open('empresas.txt', 'w') as fsalida:
            fsalida.write(str_empresas)
        print("="*ANCHO)

    else:
        print("="*ANCHO)
        print(" "*10 + "OPCIÓN INVÁLIDA")
        print("="*ANCHO)

    time.sleep(1)
