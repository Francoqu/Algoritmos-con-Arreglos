Codificación de Algoritmos con Arreglos
Introducción
Esta actividad tiene como objetivo desarrollar habilidades prácticas en el uso de matrices para implementar algoritmos en Python. Para hacer esto, resolvemos problemas comunes como encontrar elementos (valores máximos y mínimos) y ordenar datos usando dos algoritmos de clasificación básicos: clasificación por burbujas y clasificación por selección. Además, se creó un repositorio de GitHub para documentar y compartir el proyecto.

Problemas Abordados
Se implementaron funciones para encontrar el elemento mayor y menor en un arreglo de enteros. Esto es útil en muchos problemas donde necesitamos evaluar rápidamente el rango de valores en un conjunto de datos.
Se utilizó Bubble Sort y Selection Sort para ordenar un arreglo de números enteros. Estos algoritmos de ordenación sirven como ejemplos básicos para entender los principios de ordenación sin el uso de bibliotecas o métodos avanzados.

Bubble Sort
Ordena los elementos comparando pares adyacentes y cambiándolos si están en el orden incorrecto. Este proceso se repite hasta que el arreglo esté completamente ordenado. Es un algoritmo de ordenación de tipo O(n²), lo que significa que no es eficiente para grandes conjuntos de datos.
Selection Sort
Encuentra el elemento más pequeño en el arreglo y lo coloca en la primera posición. Luego, repite el proceso para el resto del arreglo. Es más eficiente que Bubble Sort en ciertos casos, aunque ambos tienen la misma complejidad en el peor de los casos: O(n²).

Conclusiones 
Tanto los algoritmos de clasificación por burbujas como los de clasificación por selección tienen una complejidad de O (n²) en el peor de los casos, lo que los hace ineficientes para matrices grandes. Sin embargo, estos algoritmos son útiles para comprender los conceptos básicos de clasificación y procesamiento de datos pequeños. La implementación de estos algoritmos básicos le permite analizar la cantidad de comparaciones y movimientos de datos que realizan, una habilidad clave cuando se trabaja con algoritmos más avanzados.

Desafíos 
Uno de los principales desafíos es optimizar la implementación para que el algoritmo funcione correctamente dada cualquier entrada válida. Es especialmente importante manejar casos especiales como matrices vacías o matrices con elementos duplicados.

Organización del Proyecto en GitHub
Estructura del Repositorio
El código está organizado en carpetas que facilitan su comprensión y mantenimiento. La carpeta Código contiene el código fuente.
1.	README.md
Se creó un archivo README detallado que incluye:
o	Descripción de los problemas abordados.
o	Instrucciones para ejecutar el código.
o	Ejemplos de entrada y salida de los casos de prueba.
o	Reflexiones sobre la eficiencia de los algoritmos implementados.

Conclusión
Esta actividad proporciona una base sólida para comprender el uso de matrices en Python y una introducción a los algoritmos de clasificación. Los archivos y la organización de GitHub no solo facilitan la colaboración en equipo, sino que también sirven como recursos de aprendizaje para proyectos futuros.




## Codificación de Algoritmos con Arreglos

### Problemas Abordados
- Búsqueda de elementos máximo y mínimo en un arreglo.
- Ordenación de un arreglo usando Bubble Sort y Selection Sort.

### Algoritmos Implementados
- **Búsqueda de mayor y menor**: Funciones que encuentran el valor más alto y más bajo en un arreglo.
- **Bubble Sort**: Algoritmo de ordenación que intercambia elementos adyacentes repetidamente.
- **Selection Sort**: Algoritmo de ordenación que selecciona el elemento más pequeño y lo coloca en su posición correcta.

### Instrucciones para Ejecutar
- Clona el repositorio y ejecuta el archivo `algoritmos.py`.

### Ejemplos de Entrada y Salida
- Entrada: `[34, 12, 45, 2, 18, 29]`
- Salida:
  - Mayor: `45`
  - Menor: `2`
  - Bubble Sort: `[2, 12, 18, 29, 34, 45]`
  - Selection Sort: `[2, 12, 18, 29, 34, 45]`
