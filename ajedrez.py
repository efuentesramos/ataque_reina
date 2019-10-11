import string


def main():
    correcto=0

    while correcto!=1 :
          nombrearchivo = input("escriba la ruta y el nombre del archivo txt ")
          try:
                archivo= open(nombrearchivo,"r")
                datos = archivo.read()  # "datos" es una cadena para guardar el texto del archivo
                archivo.close()
                correcto=1
          except:
                 print("no existe archivo o la ruta erronea")
    numero = queensattack(datos)
    if numero ==0:
        print("los valores para n y k deben estar en los siguientes rangos :if (0<n<=100000) and (0<=k<=100000): ")
    else :
         print("el numero de posiciones posibles para atacar son  :  ",numero)

def queensattack (cad_valores):
    valores = cad_valores.split() #valores es una lista con los datos suministrados a la funcion
    n=int(valores[0])        # n=numero de filas y columnas del tablero ,k= numero de obstaculos,r_q=fila reina,c_q=columna de la reina
    k=int(valores[1])
    r_q= int(valores[2])
    c_q=int(valores[3])
    trayectoria = ("up","dow","left","raight","diag1_up","diag1_dow","diag2_up","diag2_dow") # tupla para guardar tipos de desplazientos
    sentido=""
    pos_attack=0                  #pos_attack es un contador para llevar el numero de las posiciones de ataque que tendria la reina
    cord_lim=0                    #cord_lim permite llevar un control de acerdamiento a los bordes en desplazamientos verticales y horizontales
    diag_fil=0                    #diag_col y dig_fil permite llevar un control de acerdamiento a los bordes en desplazamientos diagonales
    diag_col=0
    chessboard=[]                #matriz para representar tablero de ajedrez
    obstacles=[]                 #arreglo para guardar las pociciones de los obstaculos que tendra la reina en su desplazamientos
    incr_valores=0
    if (0<n<=10**5) and (0<=k<=10**5):

       for i in range(n):                     #Se crea la matriz que que simulara el trablero de ajedrez
          a= [0]*n                            #se hace mediente un ciclo adicionando una lista de "n" elementos "n" veces
          chessboard.append(a)
       chessboard[r_q-1][c_q-1]=1
       for i in range(k):                    #Se crea la matriz que que almacenara las pociciones de los obstaculos que tendra
            ob=[0]*2                         #la reina para dezplazarse,se hace mediente un ciclo adicionando una lista de "2"
            obstacles.append(ob)             #elementos "k" veces(de acuerdo al numero de obstaculos presentes
            for j in range(2):
               incr_valores=incr_valores+1                                  #en este ciclo interno se va asignando valor de "1"
               obstacles[i][j]=int(valores[3+incr_valores])                 #por cada posicion de los obstaculos
            if (r_q != obstacles[i][j - 1])and(obstacles[i][j] != c_q):     #si valida que un obstaculo no ocupe la posicion de la reina
                 chessboard[(obstacles[i][j-1])-1][(obstacles[i][j])-1]=1
       for sentido in trayectoria :
              if sentido =="up":                                #se implementa un ciclo for que itera sobre los valores de la tupla trayectoria
                   cord_lim =r_q-1                              #la variable "sentido" toma uno de estos valores(arriba, abajo, a los lados y diagonales)
                   while cord_lim<(n-1):                        #donde entra en un conjunto de condiciones tipo swithc y se ejecuta el algoritmo respectivo
                        cord_lim = cord_lim + 1                 #para cada condicion
                        if chessboard[cord_lim][c_q-1]==0:
                           pos_attack=pos_attack+1
                        else :
                              cord_lim=n
              elif sentido=="dow":                                 #las primeras 4 condiciones permiten un recorrido vertical y horizontal respectivamente
                    cord_lim= r_q - 1                              #el vertical manteniene constante el valor de la colunma y el de la fila varia
                    while cord_lim >0:                             #el horizontal mantiene constante el valor de la fila y el de la columna varia
                          cord_lim =cord_lim - 1                   #el contador de posiciones de ataque por cada celda "libre" representada por un 0 se
                          if chessboard[cord_lim][c_q-1] == 0:     #incrementa hasta encontrar un obstaculo ó llegue al borde del tablero o matriz
                               pos_attack = pos_attack + 1
                          else:
                              cord_lim=0

              elif sentido=="raight":
                    cord_lim=c_q-1
                    while cord_lim < (n - 1):
                        cord_lim = cord_lim + 1
                        if chessboard[r_q-1][cord_lim] == 0:
                            pos_attack = pos_attack + 1
                        else:
                            cord_lim = n

              elif sentido=="left":
                   cord_lim= c_q - 1
                   while cord_lim >0:
                         cord_lim = cord_lim - 1
                         if chessboard[r_q-1][cord_lim] == 0:
                              pos_attack = pos_attack + 1
                         else:
                             cord_lim=0
              elif sentido=="diag1_up":
                   diag_fil=r_q-1
                   diag_col = c_q - 1
                   while diag_fil < (n - 1) and diag_col<(n-1):
                       diag_fil= diag_fil + 1
                       diag_col=diag_col +1
                       if chessboard[diag_fil][diag_col] == 0:
                           pos_attack = pos_attack + 1                 #las ultimas 4 condiciones permiten un recorrido en diagonales
                       else:                                           #en todos los sentidos de las diagonales los valores de las filas y columnas varian
                           diag_fil = n                                #segun el sentido del desplazamiento,
                           diag_col=n                                  #el contador de posiciones de ataque por cada celda "libre" representada por un 0 se
              elif sentido=="diag1_dow":                               #incrementa hasta encontrar un obstaculo ó llegue al borde del tablero o matriz
                    diag_fil=r_q-1
                    diag_col =c_q - 1
                    while diag_fil >0 and diag_col>0:
                        diag_fil= diag_fil - 1
                        diag_col=diag_col -1
                        if chessboard[diag_fil][diag_col] == 0:
                            pos_attack = pos_attack + 1
                        else:
                            diag_fil = 0
                            diag_col=0
              elif sentido=="diag2_up":
                    diag_fil=r_q-1
                    diag_col = c_q - 1
                    while diag_fil < (n - 1) and diag_col>0:
                        diag_fil= diag_fil + 1
                        diag_col=diag_col -1
                        if chessboard[diag_fil][diag_col] == 0:
                            pos_attack = pos_attack + 1
                        else:
                            diag_fil = n
                            diag_col=0

              elif sentido == "diag2_dow":
                  diag_fil = r_q-1
                  diag_col = c_q - 1
                  while diag_fil > 0 and diag_col < (n - 1):
                      diag_fil = diag_fil - 1
                      diag_col = diag_col + 1
                      if chessboard[diag_fil][diag_col] == 0:
                          pos_attack = pos_attack + 1
                      else:
                          diag_fil = 0
                          diag_col = n
       return (pos_attack)
    else:
      return (0)
if __name__ == '__main__':
     main()