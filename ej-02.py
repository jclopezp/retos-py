# isinstance(3, int) -> True
# isinstance(3, str) -> False

# x es un elemento del rango
def multiplos(a, b):
    lista = [a * x for x in range(1, b + 1)]
    return lista
