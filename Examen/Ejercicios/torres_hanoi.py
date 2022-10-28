def mover_disco(torre_inicio, torre_destino):
    print(f"moving disk from {torre_inicio} to {torre_destino}")

def TorreHanoi(n, torre_inicio, torre_destino, torre_aux):
    if n < 1:
        return
    TorreHanoi(n - 1, torre_inicio, torre_aux, torre_destino)
    mover_disco(torre_inicio, torre_destino)
    TorreHanoi(n - 1, torre_aux, torre_destino, torre_inicio)

if __name__ == "__main__":
    TorreHanoi(64, 'A', 'B', 'C')