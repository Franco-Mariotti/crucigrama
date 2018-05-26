def inicializar_fila(caracter,lng):
	""""""
	fila = [caracter for _ in range(lng)]
	return fila

def generar_filas_crucigrama_superior(repr_crucigrama,i_max,palabra,item,imprimir_solucion):
	""""""
	fila = repr_crucigrama
	maximo_vertical = item[1][1]
	if(maximo_vertical >= i_max and imprimir_solucion):
		fila[item[1][0]] = palabra[abs(i_max - maximo_vertical)]
	elif(maximo_vertical >=i_max):
		fila[item[1][0]] = "."
	return fila

def generar_filas_crucigrama_inferior(repr_crucigrama,contador,palabra,item,imprimir_solucion):
	""""""
	fila = repr_crucigrama
	minimo_vertical = item[1][1] + contador
	if(minimo_vertical < len(palabra) and imprimir_solucion):
		fila[item[1][0]] = palabra[minimo_vertical]
	elif(minimo_vertical < len(palabra)):
		fila[item[1][0]] = "."
	return fila

def imprimir_filas_crucigrama(contador,crucigrama,extremo,iterar,validar,generar_fila,imprimir_solucion): 
	""""""
	while(validar(contador,extremo)):
		repr_crucigrama = inicializar_fila(" ",len(crucigrama["H"][0]))

		for item in crucigrama.items():
			palabra = item[0] 	
			if(palabra == "H"):
				continue
			repr_crucigrama = generar_fila(repr_crucigrama,contador,palabra,item,imprimir_solucion)
		print("".join(repr_crucigrama))
		del repr_crucigrama
		contador = iterar(contador)

def imprimir_representacion_crucigrama(crucigrama,maximo,minimo,imprimir_solucion):
	""""""

	imprimir_filas_crucigrama(maximo,crucigrama,maximo,lambda x: x - 1,lambda x,y:x,generar_filas_crucigrama_superior,imprimir_solucion)
	if(imprimir_solucion):
		print("{} {}".format("H",crucigrama["H"][0])) #crucigrama["H"]-Horizontal del crucigrama"
	else:
		sl_horizontal = "".join(inicializar_fila(".",len(crucigrama["H"][0])))
		print("{} {}".format("H",sl_horizontal))
	imprimir_filas_crucigrama(1,crucigrama,minimo,lambda x:x + 1,lambda x,y: x <= y,generar_filas_crucigrama_inferior,imprimir_solucion)
	
