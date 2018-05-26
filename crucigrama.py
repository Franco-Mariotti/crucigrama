import random
import os

LNG_MIN_HORZ=8

def buscar_pos_letra_en_palabra(palabra,letra):
	for i in range(len(palabra)):
		if(palabra[i] == letra):
			return i

def imprimir_definiciones_palabras(crucigrama):
	"""Recibe un crucigrama(diccionario) """
	print("{}.{}".format("H",crucigrama["H"][1]))
	for i,clave in enumerate(crucigrama.keys()):
		if(clave != "H"):
			print("{}.{}".format(i,crucigrama[clave][2]))
	print()
def es_mayor_igual_a_lng_min_horizontal(palabra):
	""""""
	return (len(palabra) >= LNG_MIN_HORZ)
def leer_linea_archivo_al_azar(archivo_palabras,tamanio_archivo,validar_palabra):
	""""""
	punto_rnd = random.randint(0,tamanio_archivo)		
	archivo_palabras.seek(punto_rnd)
	archivo_palabras.readline()
	while(archivo_palabras):
		linea = archivo_palabras.readline().decode('utf-8').split('|') #linea = (palabra,definicion)
		if(validar_palabra(linea[0])): #linea[0]=palabra
			linea[1] = linea[1].rstrip("\n")#linea[1] = definicion
			return tuple(linea)
def leer_palabra_archivo_secuencial(archivo_palabras,tamanio_archivo):
	""""""
	linea = archivo_palabras.readline().decode('utf-8').split('|') #linea = (palabra,definicion)
	print(linea)
	linea[1] = linea[1].rstrip("\n")#linea[1] = definicion
	return tuple(linea) 

def obtener_maximo_n1_n2(n1,n2):
	""""""
	es_mayor = (n1 > n2)
	if(es_mayor):
		return n1
	return n2
def buscar_coincidencia_en_vertical(letras,vertical):
	for i_l in range(len(letras)):
		if(letras[i_l] in vertical):
			return i_l
	return -1
def obtener_verticales_crucigrama(palabras,tamanio_archivo,crucigrama):
	i=0
	maximo = 0
	minimo = 0
	horizontal = crucigrama["H"][0]
	while(i<len(horizontal)):
		letras = horizontal[i:i+2]
		linea = leer_linea_archivo_al_azar(palabras,tamanio_archivo,(lambda x: x not in crucigrama.keys()))
		coincidencia = buscar_coincidencia_en_vertical(letras,linea[0])
		while(coincidencia<0):
			linea = leer_palabra_archivo_secuencial(palabras,tamanio_archivo)
			coincidencia = buscar_coincidencia_en_vertical(letras,linea[0])
		i+=coincidencia
		cantidad_filas_arriba = buscar_pos_letra_en_palabra(linea[0],horizontal[i])
		maximo = obtener_maximo_n1_n2(maximo,cantidad_filas_arriba)
		cantidad_filas_abajo = len(linea[0]) - cantidad_filas_arriba -1
		minimo = obtener_maximo_n1_n2(cantidad_filas_abajo,minimo)
		crucigrama[linea[0]] = (i,cantidad_filas_arriba,linea[1])
		i+=2	
	return maximo,minimo

def generar_crucigrama(ruta_palabras):
	""""""
	crucigrama = {}
	
	with open(ruta_palabras,"rb") as palabras:
		tamanio = os.path.getsize(ruta_palabras)
		crucigrama["H"] = leer_linea_archivo_al_azar(palabras,tamanio,es_mayor_igual_a_lng_min_horizontal)##crucigrama["H"] = Horizontal de mi crucigrama
		maximo,minimo = obtener_verticales_crucigrama(palabras,tamanio,crucigrama)
		return crucigrama,maximo,minimo

