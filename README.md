# Codificación de Algoritmos con Arreglos

## Introducción
Esta actividad tiene como objetivo desarrollar habilidades prácticas en el uso de arreglos para implementar algoritmos en Python. Aborda problemas comunes como la búsqueda de valores máximos y mínimos, y la ordenación de datos usando dos algoritmos básicos: Bubble Sort y Selection Sort. Además, se creó un repositorio en GitHub para documentar y compartir el proyecto.

## Problemas Abordados
1. **Búsqueda de elementos máximo y mínimo en un arreglo**  
   - Se implementaron funciones para encontrar el elemento mayor y menor en un arreglo de enteros, útil en problemas que requieren evaluar rápidamente el rango de valores de un conjunto de datos.

2. **Ordenación de un arreglo usando algoritmos básicos**  
   - Se utilizó Bubble Sort y Selection Sort para ordenar un arreglo de números enteros, ilustrando principios básicos de ordenación sin el uso de bibliotecas avanzadas.

## Algoritmos Implementados

### Búsqueda de Mayor y Menor
- **Descripción**: Funciones que encuentran el valor máximo y mínimo en un arreglo de enteros.
- **Aplicación**: Ideal para casos donde se necesita conocer el rango de valores o detectar límites de un conjunto de datos.

### Bubble Sort
- **Descripción**: Ordena los elementos comparando pares adyacentes y cambiándolos si están en el orden incorrecto. El proceso se repite hasta que el arreglo esté completamente ordenado.
- **Complejidad**: Este algoritmo tiene una complejidad de \( O(n^2) \), lo que lo hace ineficiente para grandes conjuntos de datos.

### Selection Sort
- **Descripción**: Encuentra el elemento más pequeño en el arreglo y lo coloca en la primera posición, repitiendo el proceso para el resto del arreglo.
- **Complejidad**: Similar a Bubble Sort, con una complejidad de \( O(n^2) \), pero en algunos casos puede ser más eficiente.

## Instrucciones para Ejecutar el Proyecto
1. Clona el repositorio desde GitHub.
2. Ejecuta el archivo `algoritmos.py` para probar los algoritmos con diferentes datos de entrada.

## Ejemplos de Entrada y Salida
- **Entrada**: `[34, 12, 45, 2, 18, 29]`
- **Salida**:  
  - **Mayor**: `45`  
  - **Menor**: `2`  
  - **Bubble Sort**: `[2, 12, 18, 29, 34, 45]`  
  - **Selection Sort**: `[2, 12, 18, 29, 34, 45]`  

## Conclusiones
Tanto Bubble Sort como Selection Sort presentan una complejidad de \( O(n^2) \), lo cual limita su uso en grandes conjuntos de datos. No obstante, son útiles para comprender conceptos básicos de ordenación y manipulación de datos en arreglos. Implementar estos algoritmos básicos ayuda a entender el número de comparaciones y movimientos de datos, lo cual es clave al trabajar con algoritmos más avanzados.

## Desafíos
- Optimizar la implementación para manejar correctamente cualquier entrada válida, incluyendo casos especiales como arreglos vacíos o con elementos duplicados.

## Organización del Proyecto en GitHub

### Estructura del Repositorio
El código está organizado en carpetas que facilitan su comprensión y mantenimiento:
- **Código**: Contiene el código fuente de los algoritmos implementados.

### README.md
- Incluye una descripción detallada de los problemas abordados, instrucciones para ejecutar el código, ejemplos de entrada y salida, y reflexiones sobre la eficiencia de los algoritmos.

## Conclusión
Esta actividad proporciona una base sólida para comprender el uso de arreglos en Python y una introducción a los algoritmos de ordenación. La organización del repositorio en GitHub facilita la colaboración y sirve como recurso de aprendizaje para proyectos futuros.
