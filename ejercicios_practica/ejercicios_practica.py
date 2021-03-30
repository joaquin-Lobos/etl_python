#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import sqlite3
import os
import time
import bonobo

import tabla

# Install bonobo
#   pip3 install -U bonobo 
# Crear archivo "dot"
#   bonobo inspect --graph ejercicios_clase.py > ejercicios_clase.dot
# Graphviz online
#   http://dreampuf.github.io/GraphvizOnline/
# Graphviz (dot) extension
#    Abrir el archivo .dot y presionar CTRL + SHIF + V

def extract():
    lista = range(0, 11)
    for number in lista:
        yield number
        time.sleep(1)
    # Realice un bucle que recorra una lista del 0 al 10 inclusive
    # En cada iteración de ese bucle realizar un "yield" del valor
    # tomado de la lista


def transform(x):
    multiplication = x * 5
    # Por cada número que ingrese a transform
    # multiplicarlo por 5
    yield multiplication


def load(result):
    tabla.insert_product(result)
    # Cada resultado que ingrese a este punto
    # ingresarlo como una nueva linea a un archivo
    # de texto (usando open con 'a' y write)
    # o insertando a una base de datos a elección.
    # El objetivo es que quede almacenado en un archivo
    # o una base de datos la tabla del 5


def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(extract, transform, load)
    return graph


def get_services(**options):
    return {}


if __name__ == "__main__":
    tabla.create_schema()
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
    
    print(tabla.get_product())    
