#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
#lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

f = open("mifichero.txt", 'w')# creamos el fichero
f.write("hola Mundo\n")# escribimos en el fichero
f.close()# cerramos la consulta al fichero, como buena practica

f = open('mifichero.txt', 'r+')
f.readline()
f.write('hola mundo 2\n')

f.seek(0)
print(f.read())
f.close()