personas = []


def registrar_asistencia():
    nombre = input("Ingrese el nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío")
        return

    estado = input("¿Está presente? (si/no): ").lower().strip()

    if estado != "si" and estado != "no":
        print("Debe escribir solamente 'si' o 'no'")
        return

    personas.append([nombre, estado])

    print("Asistencia registrada correctamente")


# FUNCION CON RETURN
def obtener_asistentes():
    asistentes = []

    for persona in personas:
        if persona[1] == "si":
            asistentes.append(persona[0])

    return asistentes


def ver_asistentes():
    asistentes = obtener_asistentes()

    print("\n--- PERSONAS PRESENTES ---")

    if len(asistentes) == 0:
        print("No hay personas presentes registradas")
    else:
        for nombre in asistentes:
            print(nombre)


def ver_ausentes():
    print("\n--- PERSONAS AUSENTES ---")

    hay_ausentes = False

    for persona in personas:
        if persona[1] == "no":
            print(persona[0])
            hay_ausentes = True

    if hay_ausentes == False:
        print("No hay personas ausentes registradas")


def buscar_persona():
    buscar = input("Ingrese el nombre que desea buscar: ").lower().strip()

    if buscar == "":
        print("Debe ingresar un nombre")
        return

    for persona in personas:
        if persona[0].lower() == buscar:
            print("\nNombre:", persona[0])
            print("Estado:", persona[1])
            return

    print("La persona no está registrada")


def eliminar_persona():
    nombre = input("Ingrese el nombre que desea eliminar: ").lower().strip()

    for persona in personas:
        if persona[0].lower() == nombre:
            personas.remove(persona)
            print("Persona eliminada correctamente")
            return

    print("La persona no está registrada")


def mostrar_total():
    total = len(personas)

    print("\n--- TOTAL DE PERSONAS ---")
    print("Total de personas registradas:", total)


while True:

    print("\n=======================")
    print(" REGISTRO DE ASISTENCIA")
    print("=======================")
    print("1. Marcar asistencia")
    print("2. Ver asistentes")
    print("3. Ver ausentes")
    print("4. Buscar persona")
    print("5. Eliminar persona")
    print("6. Ver total de personas")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_asistencia()

    elif opcion == "2":
        ver_asistentes()

    elif opcion == "3":
        ver_ausentes()

    elif opcion == "4":
        buscar_persona()

    elif opcion == "5":
        eliminar_persona()

    elif opcion == "6":
        mostrar_total()

    elif opcion == "7":
        print("Programa finalizado")
        break

    else:
        print("Opción no válida")