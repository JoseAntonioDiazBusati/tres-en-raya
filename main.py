
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


def comprobar_ganador(tablero_final: tuple)-> bool:
    pass


def turno_jugador():
    pass


def jugar():
    turno = 0
    while turno < 9 and comprobar_ganador():
        turno_jugador()
        turno += 1
    return turno


def main():
   tablero = generar_tablero()
   tablero_final = formar_tablero(tablero)
   print(tablero_final)

if __name__ == '__main__':
   main()
