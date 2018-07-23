import argparse
import crucigrama
import repr_crucigrama

RUTA_ARCHIVO_PALABRAS="palabras.csv"  

def main():
    parser = argparse.ArgumentParser(description='Generador de crucigramas')
    parser.add_argument('-s', '--solucion', action='store_true', help='imprimir la solución')
    args = parser.parse_args()

    imprimir_solucion = args.solucion # es True si el usuario incluyó la opción -s

    horizontal = crucigrama.buscar_horizontal(RUTA_ARCHIVO_PALABRAS)
    verticales_encontradas = crucigrama.buscar_verticales(RUTA_ARCHIVO_PALABRAS,horizontal[crucigrama.PALABRA])
    verticales,definiciones_verticales,y_max = crucigrama.elegir_verticales(horizontal[crucigrama.PALABRA],verticales_encontradas)
    print("\nCRUCIGRAMA:")
    repr_crucigrama.imprimir_indices_verticales(len(horizontal[crucigrama.PALABRA]),verticales)
    repr_crucigrama.imprimir_crucigrama(horizontal[crucigrama.PALABRA],verticales,y_max,False)
    print("\nDEFINICIONES:")
    repr_crucigrama.imprimir_definiciones_crucigrama(horizontal,definiciones_verticales)    
    if(imprimir_solucion):
        print("\nSOLUCION:")
        repr_crucigrama.imprimir_indices_verticales(len(horizontal[crucigrama.PALABRA]),verticales)
        repr_crucigrama.imprimir_crucigrama(horizontal[crucigrama.PALABRA],verticales,y_max,True)
    
main()
