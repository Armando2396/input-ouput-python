#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
#lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

f = open("mifichero.txt", 'w')# creamos el fichero
f.write("hola Mundo")# escribimos en el fichero
f.close()# cerramos la consulta al fichero, como buena practica

fichero = open("mifichero.txt")# almacenamos los datos en fichero
print(fichero.read())# leemos los datos por consola de mifichero.txt