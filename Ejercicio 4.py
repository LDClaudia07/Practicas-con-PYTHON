# EJERCICIOS DE TUPLAS CON PYTHON

# Ejercicio 1: Crear una tupla con los nombres de mis amigos.
amigos = ("Ana", "Mateo", "Pablo")
print(f"Los amigos son {', '.join(amigos)}")

#EJERCICIO 2
mitupla=("juan", 13,1,1995)
print(mitupla[1])

#EJERCICIO 3 TUPLAS CON LISTA
mitupla = list(mitupla)
print(mitupla)

#EJERCICIO 4 convertir una LISTA en TUPLAS
milista=["juan",13,1,1995]
mitupla=tuple(milista)
print(mitupla)

#Ejercicio 5 comprobar si el elemento existe
print("juan" in mitupla)