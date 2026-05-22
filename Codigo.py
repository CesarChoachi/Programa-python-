
# ============================================================
# Fase 5 - Evaluacion Final POA
# Problema 1: Evaluacion de nivel de compromiso de sesiones
# Nombre: Cesar Fabian Choachi Salamanca
# Codigo: 80218967
# Programa: Ingenieria
# Fecha: 22/05/2026
# ============================================================


def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


def ingresar_datos():
    matriz = []
    print("=" * 50)
    print("   INGRESO DE DATOS DE SESIONES DE CLIENTES")
    print("=" * 50)
    n = int(input("Ingrese el numero de sesiones a registrar (minimo 5): "))
    while n < 5:
        print("Debe ingresar al menos 5 sesiones.")
        n = int(input("Ingrese el numero de sesiones a registrar (minimo 5): "))

    for i in range(n):
        print(f"\n--- Sesion {i + 1} ---")
        id_cliente = input("ID del cliente: ")
        duracion = float(input("Duracion de la sesion en segundos: "))
        clics = int(input("Numero de eventos clic: "))
        matriz.append([id_cliente, duracion, clics])

    return matriz


def mostrar_informe(matriz):
    print("\n" + "=" * 50)
    print("   INFORME DE NIVEL DE COMPROMISO DE SESIONES")
    print("=" * 50)
    print(f"{'ID Cliente':<15} {'Duracion (s)':<15} {'Clics':<10} {'Clasificacion'}")
    print("-" * 50)

    for sesion in matriz:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        clasificacion = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<15} {duracion:<15} {clics:<10} {clasificacion}")

    print("=" * 50)
    print("\n--- Informacion del estudiante ---")
    print("Nombre:   Cesar Fabian Choachi Salamanca")
    print("Codigo:   80218967")
    print("Programa: Ingenieria")
    print("Fecha:    22/05/2026")
    print("=" * 50)
    input("\nPresione ENTER para salir...")


# -------------------------------------------------------
# Ejecucion principal
# -------------------------------------------------------
datos = ingresar_datos()
mostrar_informe(datos)