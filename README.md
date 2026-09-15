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