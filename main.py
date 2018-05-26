import rg_crucigrama
import crucigrama
import argparse

def main():

	parser = argparse.ArgumentParser(description='Generador de crucigramas')
	parser.add_argument('-s', '--solucion', action='store_true', help='imprimir la solución')
	args = parser.parse_args()

	imprimir_solucion = args.solucion # es True si el usuario incluyó la opción -s

	crucigrama_generado,maximo,minimo = crucigrama.generar_crucigrama("palabras.csv")
	print("\nCRUCIGRAMA:")
	rg_crucigrama.imprimir_representacion_crucigrama(crucigrama_generado,maximo,minimo,False)
	print("\nDEFINICIONES:")
	crucigrama.imprimir_definiciones_palabras(crucigrama_generado)
	if(imprimir_solucion):
		print("\nSOLUCION:")
		rg_crucigrama.imprimir_representacion_crucigrama(crucigrama_generado,maximo,minimo,imprimir_solucion)

main()