#!/usr/bin/python3

numero_estantes = int(input())
estante_medicamentos = list(map(int, input().split(" ")))

# contamos el tiempo inicial de moverse a la primera tarea
tiempo = estante_medicamentos[0] - 1  # El -1 es porque empiezo en la casa 1

for i in range(len(estante_medicamentos)-1):
    # caso que el estante sea superior a la de la siguiente
    if (estante_medicamentos[i] > estante_medicamentos[i+1]):
      tiempo = tiempo + estante_medicamentos[i+1] + numero_estantes - estante_medicamentos[i]    
    else:  #caso menor o igual
      tiempo = tiempo + estante_medicamentos[i+1] - estante_medicamentos[i]

# añado el tiempo para llegar de nuevo al mostrador
tiempo = tiempo + numero_estantes - estante_medicamentos[len(estante_medicamentos)-1] + 1

print(tiempo)