import random
def dado():
    """asigna un valor al azar entre 1 a 5
    (None)->int
    """
    r=random.randint(1,5)
    return r
def opciondado(g,m,bb):
    """Direcciona a la accion segun numero de dado
    (int, list) -> 
    """
    if g == 1:
        if m[0]:
            print("Bloqueada")
            pass
        else:
            return izquierda(bb)
    elif g == 2:
        if m[3]:
            print("Bloqueada")
            pass
        else:
            return mitad(bb)
    elif g == 3:
        if m[6]:
            print("Bloqueada")
            pass
        else:
            return derecha(bb)
    elif g == 4:
        return cuatro(bb)
    elif g == 5:
        return cinco(bb)

def azar():
    """genera un numero al azar
    (None)-> int
    """
    s=random.randint(1,100)
    return s
    
def baraja():
   
    """entrega 7 cartas al azar
    (None)->list
    """
    lista=[]
    for i in range(0,7):
        lista.append(azar())
      
    return lista

def ordasc(aa):
    for i in range(0, len(aa) - 1):
        if aa[i] > aa[i + 1]:
            return False
    return True

def duplicados(w):
    """determina si hay valores duplicados en la lista
    (list)-> bool
    """
    i = 0
    while i < len(w):
        j = i + 1
        while j < len(w):
            if w[i] == w[j]:
                return True
            j = j + 1
        i = i + 1
    return False


def izquierda(a):
    """cambia la primera carta a la izquiera por una nueva al azar
    (List)->list
    """
    for i in range(0,7):
        a[0]= azar()
    return a

def mitad(q):
    """cambia la carta de la mitad por una nueva al azar
    (List)->list
    """
    for i in range(0,7):
        q[3]=azar()
    return q

def derecha(n):
    """funcion que cambia la ultima carta a la derecha por una nueva al azar
    (List)->list
    """
    for i in range(0,7):
        n[6]=azar()
    return n
def cuatro(h):
    """Ejecuta la accion destinada a la opcion ciuatro dada por el dado
    (list) -> list
    """
    a = int(input("Ingrese el valor de la posicion de la carta"))
    h[a] = True
def cinco(v):
    """Ejecuta la accion destinada a la opcion cinco dada por el dado
    (list) ->
    """
    print("Elige alguna de las siguientes opciones")
    print("1. Intercambiar dos cartas contiguas (adyacentes)")
    print("2. Intercambiar dos cartas con dos cartas intermedias, esta opción no está disponiblepara las tres últimas cartas (derecha)")
    print("3. Rotar las cartas una posición hacia la derecha")
    print("4. Rotar las cartas una posición hacia la izquierda")
    o = int(input())
    if o == 1:
        u = int(input("Digite el numero de la posicion menor"))
        if v[u] or v[u+1]:
            print("Bloqueada")
            pass
        else:
            intercont(v)
    elif o == 2:
        p = int(input("Digite el numero de la posicion de la mitad"))
        if v[p-1] or v[p+1]:
            print("Bloqueada")
            pass
        else:
            interinter(v)
    elif o == 3:
        rotder(v)
    elif o == 4:
        rotizq(v)
def intercont(z):
    """Ejecuta la accion destinada a la opcion uno por la opcion cinco dada por el dado
    (list) -> list
    """
    a = z[u+1]
    z[u+1] = z[u]
    z[u] = a
    return a
def cinterinter(w):
    """Ejecuta la accion destinada a la opcion dos por la opcion cinco dada por el dado
    (list, int) -> list
    """
    a = w[p+1]
    w[p+1] = w[p-1]
    w[p-1] = a
    return w
def rotder(x):
    """Ejecuta la accion destinada a la opcion tres por la opcion cincodada por el dado
    (list) -> list
    """
    u = x.pop()
    x.insert(0, u)
    return x
def rotizq(w):
    """Ejecuta la accion destinada a la opcion cuatro por la opcion cincodada por el dado
    (list) -> list
    """
    p = w.pop(0)
    w.append(p)
    return w

    
def main():
    """funcion principal
    """
    t = [False, False, False, False, False, False, False]
    s=baraja()
    f=baraja()
    if duplicados(s)==True:
        s=baraja()
    print("La lista de cartas del jugador 1 es",s)
    if duplicados(f)==True:
        f=baraja()
    print("La lista de cartas del jugador 2 es", f)
    
    while ordasc(s)== False and ordasc(f)==False:
        g=input("Jugador 1, presione enter para empezar su turno")
        print("Jugador 1")
        x=dado()
        print("El numero del dado es",x)
        opciondado(x,t,s)
        print("La lista actualizada es",s)        

        w=input("Jugador 2, presione enter para su turno")
        print("Jugador 2") 
        y=dado()
        print("El numero del dado es",y)
        opciondado(y,t,f)
        print("La lista actualizada es", f)
                    
    
    if ordasc(c1) and ordasc(c2):
        print("Empate")
    elif ordasc(c1):
        print("Ganador jugador 1")
    elif ordasc(c2):
        print ("Ganador jugador 2")
main()

                





    
