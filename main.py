personas = []


def registrar_asistencia():
    nombre = input("Ingrese el nombre: ")
    estado = input("¿Está presente? (si/no): ").lower()

    personas.append([nombre, estado])

    print("Asistencia registrada correctamente")


def ver_asistentes():
    print("\n--- PERSONAS PRESENTES ---")

    for persona in personas:
        if persona[1] == "si":
            print(persona[0])


def ver_ausentes():
    print("\n--- PERSONAS AUSENTES ---")

    for persona in personas:
        if persona[1] == "no":
            print(persona[0])


def buscar_persona():
    buscar = input("Ingrese el nombre que desea buscar: ").lower()
    encontrado = False

    for persona in personas:
        if persona[0].lower() == buscar:
            print("Nombre:", persona[0])
            print("Estado:", persona[1])
            encontrado = True

    if encontrado == False:
        print("La persona no está registrada")


while True:
    print("\n=======================")
    print(" REGISTRO DE ASISTENCIA")
    print("=======================")
    print("1. Marcar asistencia")
    print("2. Ver asistentes")
    print("3. Ver ausentes")
    print("4. Buscar persona")
    print("5. Salir")

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
        print("Programa finalizado")
        break

    else:
        print("Opción no válida")