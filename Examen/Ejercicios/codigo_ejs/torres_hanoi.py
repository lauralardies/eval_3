def mover_disco(torre_inicio, torre_destino):
    ''' 
    Esta función nos imprime en pantalla el movimiento realizado de las discos 
    '''

    print('Muevo el disco desde la torre ', torre_inicio, ' a la torre', torre_destino)

def TorreHanoi(n, torre_inicio, torre_destino, torre_aux):
    '''
    Esta función calcula los movimientos a realizar por los sacerdotes
    '''

    if n < 1: # Entramos a este if si sólo hay un disco en nuestra torre de Hanoi
        return
    TorreHanoi(n - 1, torre_inicio, torre_aux, torre_destino)
    mover_disco(torre_inicio, torre_destino)
    TorreHanoi(n - 1, torre_aux, torre_destino, torre_inicio)