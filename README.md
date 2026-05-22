# Programa-python-
Contenido del README para el repositorio
Copia y pega esto exactamente en el archivo README.md de tu repositorio GitHub:

Fase 5 - Evaluación Final POA
Problema 1: Evaluación de Nivel de Compromiso de Sesiones de Clientes
Descripción
Este programa fue desarrollado como solución al Problema 1 del banco de problemas de la Fase 5 - Evaluación Final POA, correspondiente al curso de programación de la Universidad Nacional Abierta y a Distancia UNAD. El programa procesa una matriz de datos de sesiones de clientes y clasifica el nivel de compromiso de cada sesión como Alto, Medio o Bajo, con base en la duración de la sesión en segundos y el número de eventos clic registrados.


Lógica de Clasificación

Alto: Duración mayor a 180 segundos y clics mayores a 8
Medio: Todos los casos que no sean Alto ni Bajo
Bajo: Duración menor a 60 segundos o clics menores a 3

Estructura del Programa

clasificar_compromiso: Función que aplica la lógica de clasificación de cada sesión
ingresar_datos: Función que solicita al usuario los datos de cada sesión por teclado
mostrar_informe: Función que recorre la matriz y genera el informe final en consola

Requisitos

Python 3 instalado en el computador
No requiere librerías externas
