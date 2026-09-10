Registro de Asistencia

Programa de consola en Python para llevar el control de asistencia de personas (por ejemplo, en una clase, reunión o evento).

Descripción

El sistema permite registrar el nombre y estado de asistencia (presente/ausente) de cada persona, y luego consultar quiénes asistieron, quiénes no, o buscar a alguien en particular. Los datos se guardan automáticamente en un archivo asistencia.csv, así que no se pierden al cerrar el programa.

Funcionalidades

El programa presenta un menú interactivo con las siguientes opciones:

Marcar asistencia: solicita el nombre y si está presente (si/no, con validación de la respuesta). Si el nombre ya existe, ofrece actualizar su estado en vez de duplicarlo.
Ver asistentes: muestra los nombres de todas las personas marcadas como presentes y el total.
Ver ausentes: muestra los nombres de todas las personas marcadas como ausentes y el total.
Buscar persona: busca por nombre (sin distinguir mayúsculas/minúsculas) y muestra su estado de asistencia.
Ver resumen: muestra el total de registrados, presentes y ausentes.
Salir: finaliza el programa.
Requisitos
Python 3.x
No requiere librerías externas
Cómo ejecutarlo
bash
python asistencia.py

(Reemplaza asistencia.py por el nombre real del archivo .py.)

Ejemplo de uso
text
=======================
 REGISTRO DE ASISTENCIA
=======================
1. Marcar asistencia
2. Ver asistentes
3. Ver ausentes
4. Buscar persona
5. Ver resumen
6. Salir
Seleccione una opción: 1
Ingrese el nombre: Juan
¿Está presente? (si/no): si
Asistencia registrada correctamente
Estructura de datos

Cada persona se almacena en memoria como una sublista dentro de personas, y se refleja tal cual en asistencia.csv:

python
personas = [
    ["Juan", "si"],
    ["Ana", "no"],
]
persona[0] → nombre
persona[1] → estado ("si" o "no")
Archivo de datos

El programa crea/lee un archivo asistencia.csv en la misma carpeta del script. Cada fila representa una persona:

csv
Juan,si
Ana,no
Posibles mejoras a futuro
Exportar el resumen a un reporte (por ejemplo .txt o .pdf).
Permitir eliminar un registro.
Manejar múltiples eventos o fechas distintas en el mismo archivo.