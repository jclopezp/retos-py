# retos-python
Retos Sabatinos | Feb.20, 2021

### Code styling
- TODAS las variables y funciones son 'snake_case'
- TODAS las clases son camelCase
- TODO el codigo va comentado
- El nombre de las variables, funciones, clases tiene que ser legible

## Ejercicio 1
Crear una función que reciba un número como argumento y devuelva el largo de este número.

**Ejemplo**
number_length(10) -> 2
number_length(10000) -> 5
number_length(4321) -> 4

**Restricciones**
- El número no puede ser negativo
- El número que se manda a la función tiene que ser de tipo INT
- No se puede utilizar el metodo length

## Ejercicio 2
​
Crear una funcion que reciba dos numeros como argumentos (numero, longitud), y devolver una lista con los multiplos del numero dada la longitud
​
**Ejemplos**
​
- `list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]`
​
- `list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]`

**Notas:**
Vean que la lista contiene el numero que le pasan como argumento

**Restricciones**
- Los argumentos no puede ser negativos
- Los argumentos deben ser enteros

## Ejercicio 3
Crear una funcion que devuelva el factorial de un numero

**Ejemplos**
- `factorial(3) -> 6` (3*2*1)
- `factorial(4) -> 24` (4*3*2*1)

**Tips**

-Investigar que demonios es recursividad

## Ejercicio 4
Crear una funcion que formatee numeros 😄

**Ejemplos**

format_numer(1000) -> '1,000'

format_numer(43214124) -> '43,214,124'

**Restricciones**

- El argumento no puede ser negativo
- El argumento deben ser entero

## Ejercicio 4.1

- Agregar el separador que el usuario indique

**Ejemplo**

format_numer(1000,'#') -> '1#000'

format_numer(43214124) -> '43#214#124'

## Ejercicio 5

Crear una funcion que pluralice si un elemento se repite en una lista dada como argumento

El resultado tiene que ser un iterable (tuple, lista o set)

**Ejemplos**

pluralize(['apple','peach', 'apple']) -> ['apples','peach'] || ('apples', 'peach') || {'apples', 'peach'}

pluralize(['cat', 'dog', 'cat', 'cat', 'dog', 'rabbit']) -> ['cats','dogs', 'rabbit'] || ('cats', 'dogs', 'rabbit') || {'cats', 'dogs', 'rabbit'}

**Restricciones**

El argumento tiene que ser una lista []

## Ejercicio 6

Crear una funcion que cree cajas basadas en un argumento

**Ejemplos**

make_box(1) 
[
    "#"
]

make_box(2) 
[
    "##",
    "##",
]

make_box(3) 
[
    "###"
    "# #",
    "###",
]

make_box(4) 
[
    "####",
    "#  #",
    "#  #",
    "####",
]