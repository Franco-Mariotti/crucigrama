import random
import os

LNG_MIN_HORZ=8

def buscar_pos_letra_en_palabra(palabra,letra):
	"""Recibe una palabra(string) y una letra(char).Busca la posicion de la letra en la palabra.
	Devuelve la posicion(int) de la letra en la palabra si esta se encuentra en la misma, en 
	caso contrario devuelve -1"""
	for i in range(len(palabra)):
		if(palabra[i] == letra):
			return i
	return -1

def imprimir_definiciones_palabras(crucigrama):
	"""Recibe un crucigrama(diccionario) e imprime las definiciones de las palabras en el 
	crucigrama recibido."""
	print("{}.{}".format("H",crucigrama["H"][1]))
	for i,clave in enumerate(crucigrama.keys()):
		if(clave != "H"):
			print("{}.{}".format(i,crucigrama[clave][2]))
	print()
def es_mayor_igual_a_lng_min_horizontal(palabra):
	""""""
	return (len(palabra) >= LNG_MIN_HORZ)
def leer_linea_archivo_al_azar(archivo_palabras,tamanio_archivo,validar_palabra):
	"""Recibe un archivo con palabras y definiciones,el tamaño del archivo(bytes),y una 
	funcion para validar la palabra leida.Se posiciona en un punto random del archivo y le una 
	linea(palabra|definicion).Luego valida la palabra leida y en caso de que pase la validacion 
	se devuelve una tupla con la palabra y su correspondiente definicion."""
	punto_rnd = random.randint(0,tamanio_archivo)		
	archivo_palabras.seek(punto_rnd)
	archivo_palabras.readline()
	while(archivo_palabras):
		linea = archivo_palabras.readline().decode('utf-8').split('|') #linea = (palabra,definicion)
		if(validar_palabra(linea[0])): #linea[0]=palabra
			linea[1] = linea[1].rstrip("\n")#linea[1] = definicion
			return tuple(linea)
def leer_palabra_archivo_secuencial(archivo_palabras,tamanio_archivo):
	"""Recibe un archivo con palabras y definiciones y lee una linea del archivo.
		Devuelve una tupla con la palabra y su definicion, leidas del archivo."""
	linea = archivo_palabras.readline().decode('utf-8').split('|') #linea = (palabra,definicion)
	linea[1] = linea[1].rstrip("\n")#linea[1] = definicion
	return tuple(linea) 

def obtener_maximo_n1_n2(n1,n2):
	"""Recibe dos numero(int,int),n1 y n2, y devuelve el mayor de los dos"""
	es_mayor = (n1 > n2)
	if(es_mayor):
		return n1
	return n2
def buscar_coincidencia_en_vertical(letras,vertical):
	"""Recibe un rango de letras en la horizontal y busca si alguna de esas letras se encuentra 
	en la vertical recibida.Devuelve la posicion de la letra en el rango recibido que primero 
	coincide con alguna letra de la vertical."""
	for i_l in range(len(letras)):
		if(letras[i_l] in vertical):
			return i_l
	return -1
def obtener_verticales_crucigrama(palabras,tamanio_archivo,crucigrama):
	"""Recibe un archivo con palabras, el tamano del archivo(bytes) y crucigrama(diccionario).
		Luego busca al azar las verticales en el archivo recibido tales que coincidan con las letras de 
		la horizontal.
		Devuelve un maximo y minimo (int,int) que representan la maxima cantidad de letras 
		hacia arriba y la maxima cantidad de letras hacia abajo respectivamente."""
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
	"""Recibe una ruta del archivo el cual contiene las palabras para generar el crucigrama.
		Devuelve un diccionario(crucigrama) el cual contiene las palabras del crucigrama(horizontal y verticales),junto con el 
		maximo y minimo del crucigrama.
		Maximo: maxima cantidad de letras hacia arriba
		Minimo: maxima cantidad de letras hacia abajo

		Ej:
			Crucigrama:
			   	1   2   3     4   5

			            S         A
			        U   E         M
			        F   R         A
			    U   A   R         Z
			H   F U N D A M E N T O
			    A   O   L     I   N
			    R       L     O   A
			            O     B
			                  E
			Maximo: 4
			Minimo: 4
		"""
	crucigrama = {}
	
	with open(ruta_palabras,"rb") as palabras:
		tamanio = os.path.getsize(ruta_palabras)
		crucigrama["H"] = leer_linea_archivo_al_azar(palabras,tamanio,es_mayor_igual_a_lng_min_horizontal)##crucigrama["H"] = Horizontal de mi crucigrama
		maximo,minimo = obtener_verticales_crucigrama(palabras,tamanio,crucigrama)
		return crucigrama,maximo,minimo

