#!/user/bin/python3

# Número de articulos juntos
agrupacion = int(input())

# Número de pasillos
num_p = int(input())

huecos = []

# Por cada pasillo
for p in range(num_p):
    huecos.append([])
    num_e = int(input())

    for e in range(num_e):
        huecos[p].append([])
        num_b = int(input())

        for b in range(num_b):
            huecos[p][e].append([0])
            num_c = int(input())

            for c in range(num_c):
                # obtengo una cadena de dos números separados por espacios
                # troceo con split y convierto a entero
                num_oh = input().split()
                disponibles = int(num_oh[1]) - int(num_oh[0])
                huecos[p][e][b][0]+=disponibles


# muestro por pantalla
for p in range(num_p):
    for e in range(num_e):        
        for b in range(num_b):
            print("P {:02} E {:02} B {:03} {:03} {}".format(p, e, b, huecos[p][e][b][0], "SI" if huecos[p][e][b][0] >= agrupacion else "NO"))
            