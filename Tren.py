# Juego de trenes
import random
def bienv():
    print("Bienvenido al JUEGO DE TRNES")
    print("REGLAS")
    print("1. Cambiar primera carta (izquierda) por una nueva al azar")
    print("2. Cambiar carta de la mitad por una nueva al azar")
    print("3. Cambiar última carta (derecha) por una nueva al azar")
    print("4. Asegurar una carta")
def dado():
    """ Entrega un numero al azar de 1 a 6
    (None) -> int
    """
    r = random.randint(1,5)
    return r
def cartas():
    """Entrega las cartas aleatoriamente
    (None) -> list
    """
    a = random.randint(1,100)
    return a
def baraja():
    c = []
    for i in range(0,7):
        b = cartas()
        c.append(b)
    if duplicados(c):
        baraja()
    else:
        return c
def duplicados(l):
    """Determina si hay valores duplicados en la lista
    (list)-> bool
    """
    i = 0
    while i < len(l):
        j = i + 1
        while j < len(l):
            if l[i] == l[j]:
                return True
            j = j + 1
        i = i + 1
    return False
def ordasc(aa):
    for i in range(len(aa) - 1):
        if aa[i] > aa[i + 1]:
            return False
    return True
def opciondado(g,m,bb):
    """Direcciona a la accion segun numero de dado
    (int, list) -> 
    """
    if g == 1:
        if m[0]:
            print("Bloqueada")
            return bb, m
        else:
            return uno(bb), m
    elif g == 2:
        if m[3]:
            print("Bloqueada")
            return bb, m
        else:
            return dos(bb), m
    elif g == 3:
        if m[6]:
            print("Bloqueada")
            return bb, m
        else:
            return tres(bb), m
    elif g == 4:
        return bb, cuatro(m)
    elif g == 5:
        return cinco(bb, m)
def uno(a):
    """Ejecuta la accion destinada a la opcion uno dada por el dado
    (list) -> list
    """
    for i in range (0,7):
        a[0] = cartas()
    return a
def dos(q):
    """Ejecuta la accion destinada a la opcion dos dada por el dado
    (list) -> list
    """
    for i in range(0,7):
        q[3] = cartas()
    return q
def tres(n):
    """Ejecuta la accion destinada a la opcion tres dada por el dado
    (list) -> list
    """
    for i in range(0,7):
        n[6] = cartas()
    return n
def cuatro(h):
    """Ejecuta la accion destinada a la opcion ciuatro dada por el dado
    (list) -> list
    """
    a = int(input("Ingrese el valor de la posicion de la carta"))
    h[a] = True
    return h
def cinco(v, r):
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
            return v, r
        else:
            return intercont(v), r
    elif o == 2:
        p = int(input("Digite el numero de la posicion de la mitad"))
        if v[p-1] or v[p+1]:
            print("Bloqueada")
            return v, r
        else:
            return interinter(v), r
    elif o == 3:
        return rotder(v), r
    elif o == 4:
        return rotizq(v), r
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
    t1 = [False, False, False, False, False, False, False]
    t2 = [False, False, False, False, False, False, False]
    c1 = baraja()
    c2 = baraja()
    bienv()
    print("Baraja jugador 1")
    print(c1)
    print("Baraja jugador 2")
    print(c2)
    print("-----------------------------------------")
    while ordasc(c1) == False and ordasc(c2) == False:
        z = input("Jugador 1, presione enter para su turno")
        print("JUGADOR 1")
        x = dado()
        print("El numero del dado es", x)
        c1, t1 = opciondado(x, t1, c1)
        print(t1)
        print(c1)
        w = input("Jugador 2, presione enter para su turno")
        print("JUGADOR 2")
        y = dado()
        print("El numero del dado es", y)
        c2, t2 = opciondado(y, t2, c2)
        print(t2)
        print(c2)

    if ordasc(c1) and ordasc(c2):
        print("Empate")
    elif ordasc(c1):
        print("Ganador jugador 1")
    elif ordasc(c2):
        print ("Ganador jugador 2")
main()
