#Practica de LISTA
miLista=['maria', 'pepe', 'marta', 'antonio']
print(miLista[:])

#acceder a un indice o elemento
print(miLista[3])

#acceder a una porción de la lista
print(miLista[1:3]) # 1° forma
print(miLista[:3])  # 2° forma
print(miLista[2:])  # 3° forma

#Agregar elemento a la lista al final
miLista.append('JUAN')
print(miLista[:])

#Agregar elemento a la lista al intermedio
miLista.insert(2,'SANDRA')
print(miLista[:])

#Agregar varios elemento a la lista 
miLista.extend(["CASANDRA","ANA","LUCIA"])
print(miLista[:])

print(miLista.index("LUCIA"))

# COMPROBAR SI UNA DATO SE ENCUENTRA EN LA LISTA
print("marta" in miLista)

# ELIMINACIÓN de elementos en una lista
#miLista.remove(5)
#print(miLista[:])

# ELIMINACIÓN del ultimo elementos de la lista
miLista.pop()
print(miLista[:])

# SUMAR LISTAS
miLista2=["LIDIA", "RODOLFO"]
miLista3=miLista + miLista2
print(miLista3[:])

# REPETIR LISTA
miLista4=["CAROL", "MIGUEL"]*3
print(miLista4[:])