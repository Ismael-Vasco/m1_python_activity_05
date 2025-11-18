# Actividad 5
Un instituto académico pequeño necesita un sistema local que permita gestionar toda la información de sus estudiantes, las materias disponibles, las asignaciones entre ambos y el registro de notas. El objetivo es diseñar un programa en Python que funcione a través de menús interactivos, permitiendo navegar entre las diferentes funcionalidades del sistema. Todo debe manejarse mediante listas y diccionarios, operaciones lógicas, estructuras condicionales, sumas, porcentajes y validaciones básicas.

El sistema debe iniciar mostrando el Menú Principal, desde donde el usuario podrá acceder a los siguientes módulos:
---

### 1. Gestión de Estudiantes
En este módulo el usuario podrá registrar estudiantes ingresando su información básica (como nombre, edad y documento), listar todos los estudiantes registrados, consultar un estudiante específico por su ID y eliminar estudiantes del sistema. Este apartado se encarga de manejar completamente la base de estudiantes.

### 2. Gestión de Materias
Este módulo permitirá registrar nuevas materias indicando código y nombre, listar todas las materias existentes, consultar materias por su código y eliminar materias cuando ya no sean usadas. Aquí se organiza la oferta de asignaturas disponible para el sistema.

### 3. Asignaciones (Estudiante ↔ Materias)
En este apartado el usuario podrá asignar materias a un estudiante, ver todas las materias que tiene inscritas un estudiante, consultar qué estudiantes pertenecen a una materia y retirar materias asignadas. Es el módulo responsable de la relación entre estudiantes y materias usando listas, diccionarios e identificadores cruzados.

#3# 4. Notas y Calificaciones
Desde este módulo se pueden registrar notas para un estudiante indicando porcentaje y calificación, ver todas las notas asociadas a una materia, consultar el promedio final de un estudiante basado en las ponderaciones asignadas y eliminar notas registradas. Debe incluir cálculos aritméticos como sumatorias y porcentajes.

### 5. Reportes y Estadísticas
En este módulo el usuario podrá generar reportes avanzados como promedios detallados por estudiante, encontrar al estudiante con mejor promedio, calcular el porcentaje de aprobación del grupo, obtener el promedio general del curso y visualizar un ranking ordenado por desempeño. Esto permitirá analizar el rendimiento general del sistema académico.

## Objetivo de la Actividad
Se debe implementar todas estas funciones sin interfaz gráfica, únicamente usando menús por consola, listas, diccionarios, ciclos, condicionales y operaciones matemáticas. El ejercicio tiene como propósito aplicar lógica, organización de datos y manipulación de estructuras fundamentales en Python mediante un sistema completo y funcional.

## Menu principal
Este menú central permite navegar por todas las funcionalidades del sistema: acceder a la gestión de estudiantes, administración de materias, asignaciones entre estudiantes y materias, registro y consulta de notas, generación de reportes y estadísticas, así como salir del sistema; desde aquí el usuario elige cuál módulo desea operar para continuar con los procesos relacionados al manejo académico.
```
1. Gestión de Estudiantes
2. Gestión de Materias
3. Asignaciones (Estudiante ↔ Materias)
4. Notas y Calificaciones
5. Reportes y Estadísticas
6. Salir

Seleccione una opción:
```

## 1️⃣ Menú de Gestión de Estudiantes
Este menú permite registrar nuevos estudiantes con sus datos básicos, listar todos los estudiantes existentes, consultar información detallada de un estudiante utilizando su ID, eliminar estudiantes del sistema si ya no son necesarios y finalmente regresar al menú principal; todo orientado al control individual de la base de estudiantes.
```
1. Registrar estudiante
2. Listar estudiantes
3. Consultar estudiante por ID
4. Eliminar estudiante
5. Volver al menú principal

Seleccione una opción:
```

## 2️⃣ Menú de Gestión de Materias
En este menú el usuario puede registrar nuevas materias, listar las materias disponibles, consultar una materia por su código, eliminar materias del sistema y volver al menú principal; está diseñado para administrar la oferta de asignaturas utilizada en las demás funcionalidades del sistema.
```
1. Registrar nueva materia
2. Listar materias
3. Consultar materia
4. Eliminar materia
5. Volver al menú principal

Seleccione una opción:
```

## 3️⃣ Menú de Asignaciones
Este menú permite asignar materias a un estudiante, visualizar todas las materias asociadas a un estudiante específico, consultar qué estudiantes están inscritos en una materia concreta, retirar una materia previamente asignada y regresar al menú principal; su función es gestionar completamente la relación Estudiante ↔ Materias.
```
1. Asignar materia a estudiante
2. Ver materias de un estudiante
3. Ver estudiantes por materia
4. Quitar materia a un estudiante
5. Volver al menú principal

Seleccione una opción:
```

## 4️⃣ Menú de Notas y Calificaciones
Aquí el usuario puede registrar notas para un estudiante indicando materia, porcentaje y calificación, visualizar todas las notas asociadas a una materia, consultar el promedio acumulado de un estudiante, eliminar notas específicas cuando sea necesario y volver al menú principal; este módulo controla toda la parte evaluativa del sistema.
```
1. Registrar nota para un estudiante
2. Ver notas por materia
3. Ver promedio de un estudiante
4. Eliminar una nota
5. Volver al menú principal

Seleccione una opción:
```

## 5️⃣ Menú de Reportes y Estadísticas
Este menú permite generar reportes de promedios detallados por estudiante, identificar al estudiante con el mejor promedio, calcular el porcentaje de aprobación del grupo, obtener el promedio general de todos los estudiantes, ver un ranking organizado por desempeño y regresar al menú principal; su propósito es ofrecer análisis global y comparativo del rendimiento académico.
```
1. Promedios detallados por estudiante
2. Estudiante con mejor promedio
3. Porcentaje de aprobación del grupo
4. Promedio general del grupo
5. Ranking de estudiantes
6. Volver al menú principal

Seleccione una opción:
```