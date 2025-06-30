from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("\n Calculadora Open Source")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Sumar X números (avanzado)")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {sumar(a, b)}")
    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {restar(a, b)}")
    elif opcion == "3":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {multiplicar(a, b)}")
    elif opcion == "4":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {dividir(a, b)}")
    elif opcion == "5":
        numeros = list(map(float, input("Ingrese números separados por espacio: ").split()))
        print(f"Resultado: {suma_avanzada(numeros)}")
    elif opcion == "6":
        print("Adios")
        break
    else:
        print("Opción inválida. Intente nuevamente.")