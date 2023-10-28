#!/user/bin/python3
min_capacidad_global = 0

num_casos = int(input())

for caso in range(num_casos):
  # Número de paradas
  num_paradas = int(input())
  capacidad_actual = 0
  min_capacidad = 0

  for p in range(num_paradas):
    # obtengo una cadena de dos números separados por espacios
    # troceo con split y convierto a entero
    carga = input().split()
    capacidad_actual = capacidad_actual - int(carga[0]) + int(carga[1])

    min_capacidad = max(capacidad_actual,min_capacidad)

  min_capacidad_global = max(min_capacidad_global,min_capacidad)

print(min_capacidad_global)
            