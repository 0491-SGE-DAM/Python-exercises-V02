#!/usr/bin/python3

import functools, math

data = list(input().split(','))
number_data = len(data)

# es importante recordar que los itereador se "pierden" una vez se usan
# si se quieren guardar podemos almacenarlos en una lista o tupla o similar
dt = math.sqrt(functools.reduce(lambda x,y : x+y, 
                      map(lambda x: (x - functools.reduce(lambda x,y : x+y ,map(lambda x: int(x), data))/number_data)**2, 
                          map(lambda x: int(x), data)))/number_data)

print(f'{dt:0.4f}')
