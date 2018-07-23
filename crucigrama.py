import csv
import random

LONGITUD_MINIMA_HORIZONTAL=8
PALABRA=0
DEFINICION=1
HORIZONTAL="horizontal"

def elegir_verticales(horizontal,posibles_verticales):
    """Recibe horizontal(cadena) y posibles_verticales(diccionario) que contiene 
    todas las posibles verticales encontradas para armar el crucigrama.
    Devuelve verticales(lista) con las verticales seleccionadas, definiciones(lista) que contiene las
    definiciones de las verticales y y_max que representa la maxima altura por encima de la 
    horizontal del crucigrama."""
    verticales=[]
    definiciones=[]
    contador=0
    y_max = 0
    while(contador < len(horizontal)):
        letra_horizontal = horizontal[contador]
        if(len(posibles_verticales[letra_horizontal]) == 0):
            contador+=1
            continue
        registro = posibles_verticales[letra_horizontal].pop()
        vertical = registro[PALABRA]
        y = vertical.find(letra_horizontal)
        if(y_max < y):
            y_max = y
        verticales.append((contador,y,vertical))
        definiciones.append(registro[DEFINICION])
        contador+=2
    return verticales,definiciones,y_max


def buscar_horizontal(ruta_archivo_palabras):
    """Recibe ruta_archivo_palabra(string) que representa la direccion donde se encuentra el archivo.
        Devuelve una palabra de longitud mayor igual a LONGITUD_MINIMA_HORIZONTAL"""
    with open(ruta_archivo_palabras,encoding="utf-8") as palabras:
        lector_palabras = csv.reader(palabras,delimiter="|")
        horizontales = []
        for registro in lector_palabras:
            if(len(registro[PALABRA]) >= LONGITUD_MINIMA_HORIZONTAL):
                horizontales.append(registro)
        return random.choice(horizontales)    

def buscar_letra_horizontal_en_vertical(vertical,letras_horizontal):
    """Recibe vertical(string) y letras_horizontal(diccionario) que contiene como claves las 
    letras de la horizontal.
    Devuelve la letra de la horizontal con la cual la vertical recibida coincide."""
    for letra in vertical:
        if(letra in letras_horizontal):
            return letra

def inicializar_contador_letras_en_palabra(palabra):
    """
    Recibe una palabra(string).
    Devuelve un diccionario que contiene como clave las letras de la palabra y
    como valores la cantidad de veces que esa letra se repite en la palabra.
    """
    contador_letras= {}
    for letra in palabra:
        if(letra in contador_letras):
            contador_letras[letra] +=1
        else:
            contador_letras[letra]=1
    return contador_letras

def buscar_verticales(ruta_archivo_palabras,horizontal):
    """Recibe ruta_archivo_palabra(string) que representa la direccion donde se encuentra 
    el archivo y horizontal(string) que representa la horizontal del crucigrama.
    Devuelve una lista con las verticales seleccionadas de manera random en el archivo."""
    #Cuenta cuantas veces se repite una letra en la horizontal
    contador_letras = inicializar_contador_letras_en_palabra(horizontal)
    #Lista de verticales,asignadas por letra de vertical con la que coincide
    verticales={letra:[] for letra in horizontal}
    with open(ruta_archivo_palabras,encoding="utf-8") as palabras:
        lector_palabras = csv.reader(palabras,delimiter="|")
        contador=0
        for registro in lector_palabras:
            letra = buscar_letra_horizontal_en_vertical(registro[PALABRA],verticales)
            if(not letra or horizontal == registro[PALABRA]):
                continue
            #Chequea que haya una vertical por cada letra de la horizontal
            if(len(verticales[letra])<contador_letras[letra]): 
                verticales[letra].append(registro)
            else:
                probabilidad = random.randint(1,contador)
                if(probabilidad <= len(horizontal)):
                    #Para el caso en que un letra tenga asignado mas de una palabra, 
                    #se dicide aleatoriamente cual reemplazar.
                    elemento_a_reemplazar = random.choice(range(contador_letras[letra]))
                    verticales[letra][elemento_a_reemplazar] = registro
            contador+=1
        return verticales
