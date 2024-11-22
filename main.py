def generar_tablero()-> tuple:
   """

   """
   filas = 3
   columnas =  3
   fila = []
   for i in range(filas):
       columna = []
       for j in range(columnas):
           columna.append(" ")
       fila.append(columna)
   return tuple(fila)


def formar_tablero(tablero: tuple)-> tuple:
   """

   """
   tablero_final = ""
   separador = "-"*(4*(len(tablero[0])))+"-"+"\n"
   for fila in tablero:
       tablero_final += separador + "| " + " | ".join(map(str, fila))+" |"+"\n"
   return tablero_final+separador


def main():
   tablero = generar_tablero()
   print(formar_tablero(tablero))


if __name__ == '__main__':
   main()
