# 📋 Registro de Asistencia

## 📌 Descripción

Este proyecto es un programa de **registro de asistencia** desarrollado en Python.

El programa permite registrar personas indicando si están presentes o ausentes. También permite consultar los asistentes, consultar los ausentes, buscar una persona, eliminar una persona y conocer el total de personas registradas.

El proyecto utiliza funciones, listas, condicionales, ciclos `for` y `while`, además de `return` para organizar mejor el código.

---

## 🎯 Objetivo

Crear un programa sencillo que permita llevar el control de asistencia de un grupo de personas mediante un menú interactivo.

---

## ⚙️ Funcionalidades

El programa cuenta con las siguientes opciones:

1. **Marcar asistencia**
   - Permite ingresar el nombre de una persona.
   - Permite indicar si está presente (`si`) o ausente (`no`).
   - Guarda la información en una lista.

2. **Ver asistentes**
   - Muestra las personas que tienen registrada la asistencia como `si`.

3. **Ver ausentes**
   - Muestra las personas que tienen registrada la asistencia como `no`.

4. **Buscar persona**
   - Permite buscar una persona por su nombre.
   - Muestra su nombre y estado de asistencia.

5. **Eliminar persona**
   - Permite eliminar una persona de la lista de registros.

6. **Ver total de personas**
   - Muestra la cantidad total de personas registradas.

7. **Salir**
   - Finaliza el programa.

---

## 🧩 Explicación del código

### 📦 Lista `personas`

```python
personas = []

Se utiliza una lista llamada personas para almacenar los registros de asistencia.

Cada persona se guarda de la siguiente forma:

["Nombre", "si"]

o:

["Nombre", "no"]
👤 Función registrar_asistencia()

Esta función solicita el nombre de la persona y su estado de asistencia.

También verifica que el nombre no esté vacío y que el estado sea únicamente si o no.

Después agrega la información a la lista personas.

👥 Función obtener_asistentes()

Esta función fue agregada para aplicar el uso de return.

Recorre la lista de personas y guarda solamente los nombres de quienes están presentes.

return asistentes

El return permite devolver la lista de personas presentes para utilizarla en otra función.

📋 Función ver_asistentes()

Utiliza la función obtener_asistentes() para obtener la lista de personas presentes y posteriormente mostrarlas en pantalla.

❌ Función ver_ausentes()

Recorre la lista de personas y busca aquellas cuyo estado sea no.

Después muestra los nombres de las personas ausentes.

🔎 Función buscar_persona()

Permite ingresar un nombre y buscarlo dentro de la lista.

Si encuentra a la persona, muestra:

Nombre
Estado de asistencia

Si no la encuentra, muestra un mensaje indicando que no está registrada.

🗑️ Función eliminar_persona()

Busca una persona por su nombre y, si existe, la elimina de la lista utilizando:

personas.remove(persona)
🔢 Función mostrar_total()

Utiliza len() para contar cuántas personas están registradas:

total = len(personas)

Luego muestra el resultado en pantalla.

🔄 Menú principal

El programa utiliza un ciclo:

while True:

Esto permite que el menú se siga mostrando hasta que el usuario seleccione la opción 7. Salir.

Para elegir qué función ejecutar se utilizan:

if
elif
else

Por ejemplo:

if opcion == "1":
    registrar_asistencia()

Cuando el usuario selecciona 1, se ejecuta la función correspondiente.

🛠️ Conceptos utilizados

Durante el desarrollo del proyecto se utilizaron los siguientes conceptos de Python:

Variables
Listas
Funciones
Parámetros
return
Condicionales if, elif y else
Ciclos for
Ciclo while
input()
print()
append()
remove()
len()
lower()
strip()
💻 Tecnología

Lenguaje: Python

Editor: Visual Studio Code

Control de versiones: Git y GitHub

📁 Estructura del proyecto
proyecto_victor/
│
├── main.py
│
└── README.md
main.py

Contiene todo el código del programa de registro de asistencia.

README.md

Contiene la descripción, funcionamiento y explicación del proyecto.

👨‍💻 Autor

Proyecto realizado como parte de la práctica de programación.

📌 Estado del proyecto

✅ Proyecto funcional
✅ Menú interactivo
✅ Uso de funciones
✅ Uso de return
✅ Registro de asistencia
✅ Búsqueda de personas
✅ Eliminación de personas
✅ Conteo de personas
✅ Proyecto subido a GitHub