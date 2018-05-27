def inicializar_fila(caracter,lng):
	"""Recibe un caracter(char) y crea una lista(list) con el 
	caracter recibido y de la longitud[lng(int)] recibida.
	Devuelve la lista creada."""
	fila = [caracter for _ in range(lng)]
	return fila

def imprimir_filas_crucigrama(contador,crucigrama,extremo,iterar,validar,generar_fila,imprimir_solucion): 
	"""Recibe un contador(int),un crucigrama(diccionario),un extremo(int), iterar(funcion),generar_fila(funcion),e imprimir_solucion(booleano).
		Esta funcion se encarga de imprimir todas las filas generadas por las funcion generar fila, la cual devuelve la 
		representacion de cada fila del crucigrama."""
	while(validar(contador,extremo)):
		repr_crucigrama = inicializar_fila(" ",len(crucigrama["H"][0]))

		for item in crucigrama.items():
			palabra = item[0] 	
			if(palabra == "H"):
				continue
			repr_crucigrama = generar_fila(repr_crucigrama,contador,palabra,item,imprimir_solucion)
		print(" {}".format("".join(repr_crucigrama)))
		del repr_crucigrama
		contador = iterar(contador)

def imprimir_representacion_crucigrama(crucigrama,maximo,minimo,imprimir_solucion):
	"""Recibe un crucigrama(diccionario),maximo(int),minimo(int) e imprimir_solucion. 
		Genera una mtriz la cual representa graficamente el crucigrama(repr_crucigrama) con su vertical,horizontal y espacios vacios.
		Por ultimo imprime la matriz generada."""
	def __generar_filas_crucigrama_superior(repr_crucigrama,i_max,palabra,item,imprimir_solucion):
		"""Recibe una repr_crucigrama(lista), i_max(int),palabra(string),item(tupla) y imprimir_solucion(booleano).
		Devuelve una lista que representa cada fila del crucigrama, poniendo espacios vacios donde no hay ninguna letra 
		y un . donde deberia ir una letra de alguna de las verticales si solo si imprimir_solucion es False.
		En caso de que impimir_solucion es True devuelve una lista que representa cada fila del crucigrama, poniendo un espacio vacio 
		donde no hay ninguna letra en caso contrario agrega la letra de la vertical.
		"""
		fila = repr_crucigrama
		maximo_vertical = item[1][1]
		if(maximo_vertical >= i_max and imprimir_solucion):
			fila[item[1][0]] = palabra[abs(i_max - maximo_vertical)]
		elif(maximo_vertical >=i_max):
			fila[item[1][0]] = "."
		return fila

	def __generar_filas_crucigrama_inferior(repr_crucigrama,contador,palabra,item,imprimir_solucion):
		""" Recibe una repr_crucigrama(lista), contador(int),palabra(string),item(tupla) y imprimir_solucion(booleano).
		Devuelve una lista que representa cada fila del crucigrama, poniendo espacios vacios donde no hay ninguna letra 
		y un . donde deberia ir una letra de alguna de las verticales si solo si imprimir_solucion es False.
		En caso de que impimir_solucion es True devuelve una lista que representa cada fila del crucigrama, poniendo un espacio vacio 
		donde no hay ninguna letra en caso contrario agrega la letra de la vertical."""
		fila = repr_crucigrama
		minimo_vertical = item[1][1] + contador
		if(minimo_vertical < len(palabra) and imprimir_solucion):
			fila[item[1][0]] = palabra[minimo_vertical] #item[1][0] = posicion letra de la vertical en horizontal
		elif(minimo_vertical < len(palabra)):
			fila[item[1][0]] = "."
		return fila

	imprimir_filas_crucigrama(maximo,crucigrama,maximo,lambda x: x - 1,lambda x,y:x,__generar_filas_crucigrama_superior,imprimir_solucion)
	if(imprimir_solucion):
		print("{} {}".format("",crucigrama["H"][0])) #crucigrama["H"]-Horizontal del crucigrama"
	else:
		sl_horizontal = "".join(inicializar_fila(".",len(crucigrama["H"][0])))
		print("{} {}".format("",sl_horizontal))
	imprimir_filas_crucigrama(1,crucigrama,minimo,lambda x:x + 1,lambda x,y: x <= y,__generar_filas_crucigrama_inferior,imprimir_solucion)
	
