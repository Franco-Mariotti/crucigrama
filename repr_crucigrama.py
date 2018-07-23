from crucigrama import DEFINICION,PALABRA,HORIZONTAL

OCULTO="*"

def inicializar_fila(longitud_lista):
	"""Recibe longitud_lista(int) que representa la longitud de la lista a devolver.
		Devuelve una lista llena de espacios, de longitud igual a longitud_lista"""
	return list(" "*longitud_lista)
	
def imprimir_indices_verticales(longitud_horizontal,verticales):
	"""Recibe longitud_horizontal(int) que representa la longitud de lista a devolver y una 
	verticales(list) que contiene todas las verticales del crucigrama.
	Imprime una fila con numeracion de cada vertical en la posicion en que cruza a la horizontal."""

	fila = inicializar_fila(longitud_horizontal)
	for i_v,vertical in enumerate(verticales,1):
		fila[vertical[0]] = str(i_v)
	print(" \t{}".format("".join(fila)))

def elegir_caracter(letra,mostrar_solucion):
	"""Recibe letra(char) y mostrar_solucion(booleano). 
		Devuelve la letra recibida o  CARACTER_SECRETO(*) dependiendo del valor de mostrar_solucion."""
	if(mostrar_solucion):
		return letra
	return OCULTO
	
def imprimir_crucigrama(horizontal,verticales_crucigrama,y_max,imprimir_solucion):
	"""Recibe horizontal(string) que representa la horizontal del crucigrama, verticales_crucigrama(list) que 
	contiene las verticales del crucigrama junto con la posicion en que cortan a la horizontal y la posicion en 
	que la horizontal corta a la vertical.
	Imprime el crucigrama mostrando las palabras o el crucigrama oculto, dependiendo del valor de imprimir_solucion(booleano).
	"""
	#Realiza una copia de las lista de verticales recibidas pero convierte las verticales en una lista 
	#con los caracteres de la vertical invertida. Esto hace que sea mas facil imprimirla.
	verticales = [(x,y,list(vertical[::-1])) for x,y,vertical in verticales_crucigrama] 
	cadena_vacia = " "*len(horizontal)
	esta_vacia = False
	fila_actual = y_max

	while(not esta_vacia):
		fila = inicializar_fila(len(horizontal))
		for x,y,vertical in verticales:
			if(len(vertical) == 0):
				continue
			elif(y >= fila_actual):
				fila[x]= elegir_caracter(vertical.pop(),imprimir_solucion)
		salida = "".join(fila)
		if(salida == cadena_vacia):
			esta_vacia = True
		elif(fila_actual == 0):
			print("H\t{}".format("".join([elegir_caracter(letra,imprimir_solucion) for letra in horizontal])))
		else:
			print(" \t{}".format(salida))
		fila_actual-=1

def imprimir_definiciones_crucigrama(horizontal,definiciones):
	"""Recibe horizontal(string) que representa la horizontal del crucigrama y definiciones(list) 
	que contiene las definiciones de las palabras del crucigrama.
	Imprime todas las definiciones recibidas."""
	print("H.{}".format(horizontal[DEFINICION]))
	for i_d,definicion in enumerate(definiciones,1):
		print("{}.{}".format(i_d,definicion))	
    
