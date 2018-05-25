def inicializar_fila(caracter,lng):
	fila = [caracter for _ in range(lng)]
	return fila

def validacion_superior(maximo,contador):
	return maximo

def validacion_inferior(minimo,contador=0):
	return (contador<=minimo)

def generar_repr_crucigrama_superior(repr_crucigrama,contador,palabra,item,maximo,imprimir_solucion):
	fila = repr_crucigrama
	maximo_vertical = item[1][1]
	if(maximo_vertical >= maximo and imprimir_solucion):
		fila[item[1][0]] = palabra[abs(maximo - maximo_vertical)]
	elif(maximo_vertical >=maximo):
		fila[item[1][0]] = "."
	return fila

def generar_repr_crucigrama_inferior(repr_crucigrama,contador,palabra,item,minimo,imprimir_solucion):
	fila = repr_crucigrama
	minimo_vertical = item[1][1] + contador
	if(minimo_vertical < len(palabra) and imprimir_solucion):
		fila[item[1][0]] = palabra[minimo_vertical]
	elif(minimo_vertical < len(palabra)):
		fila[item[1][0]] = "."
	return fila

def imprimir_crucigrama(crucigrama,valor,validar,generar_repr_crucigrama,modo_sup,imprimir_solucion):
	contador = 1
	while(validar(valor,contador)):
		repr_crucigrama = inicializar_fila(" ",len(crucigrama["H"][0]))

		for item in crucigrama.items():
			palabra = item[0] 	
			if(palabra == "H"):
				continue
			repr_crucigrama = generar_repr_crucigrama(repr_crucigrama,contador,palabra,item,valor,imprimir_solucion)
		print("".join(repr_crucigrama))
		del repr_crucigrama
		if(modo_sup):
			valor-=1
		else:
			contador+=1


def imprimir_representacion_crucigrama(crucigrama,maximo,minimo,imprimir_solucion):
	imprimir_crucigrama(crucigrama,maximo,validacion_superior,generar_repr_crucigrama_superior,True,imprimir_solucion)
	if(imprimir_solucion):
		print(crucigrama["H"][0]) #crucigrama["H"]-Horizontal del crucigrama"
	else:
		print("".join(inicializar_fila(".",len(crucigrama["H"][0]))))
	imprimir_crucigrama(crucigrama,minimo,validacion_inferior,generar_repr_crucigrama_inferior,False,imprimir_solucion)
	
