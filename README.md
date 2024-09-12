# Manual de uso snake.py

## Caracteristicas:
Con las modificaciones realizadas, tanto la comida como la serpiente contaran con colores aleatorios definidos
De igual forma, la comida se moverá una sola celda, asegurando que no salga del espacio de la pantalla.

## `defineColors`

La función `defineColors` selecciona aleatoriamente dos colores distintos de una lista predefinida y los devuelve.

### Descripción

Esta función inicializa un arreglo de cadenas de colores. Luego, selecciona un color al azar para representar la "serpiente" y elimina este color de la lista. A continuación, se elige un segundo color al azar de los colores restantes para representar la "comida". La función devuelve estos dos colores como una tupla.

### Parámetros

- **Ninguno**

### Retorna

- **Tupla[str, str]**: Una tupla que contiene dos cadenas de colores distintos. La primera cadena es el color asignado a la serpiente, y la segunda cadena es el color asignado a la comida.

### Ejemplo

```python
snakeColor, foodColor = defineColors()
print(f"Color de la serpiente: {snakeColor}")
print(f"Color de la comida: {foodColor}")
```

### move_food
- Es una función auxiliar para mover la comida a una celda contigua, asegurando que esta no salga de la ventana
 ademas de asegurarse que la nueva posición no choque con alguna parte del cuerpo de la serpiente pera evitar errores.


### Notas

- La función utiliza la función `randrange` del módulo `random` para asegurar que la selección de colores sea aleatoria.
- Si el `colorArray` contiene menos de dos colores, la función generará un `IndexError` debido a la selección de colores de una lista vacía.
