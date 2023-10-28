#!/usr/bin/python3

# Leo una cadena y la convierto a entero
numero_estantes = int(input())

# Leo una cadena con input. La separo por espacios con split
# Con map, aplico a cada elemento la funcion int para
# convertitlo a entero
# En este caso, ademas aplico list para convertirlo en lista
articulos_en_estantes = list(map(int, input().split(" ")))
maximo = max(articulos_en_estantes)

solicitar_almacen = 0
for articulo_en_estante_i in articulos_en_estantes:
    solicitar_almacen = solicitar_almacen + (maximo - articulo_en_estante_i)

print(solicitar_almacen)

