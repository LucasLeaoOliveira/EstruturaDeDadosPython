def acomodar_reservas(reservas, salas_ocupadas):
    reservas_acomodadas = []
    for reserva in reservas:
        hora_inicio, hora_fim = reserva
        sala_encontrada = False
        for i in range(len(salas_ocupadas)):
            # Verificar se a sala está livre no intervalo de tempo da reserva
            if all(salas_ocupadas[i][j] == 0 for j in range(hora_inicio, hora_fim)):
                # Acomodar a reserva na sala i
                for j in range(hora_inicio, hora_fim):
                    salas_ocupadas[i][j] = 1
                reservas_acomodadas.append(reserva)
                sala_encontrada = True
                break
        if not sala_encontrada:
            # Não há salas disponíveis para acomodar esta reserva
            print(f"Não há salas disponíveis para acomodar a reserva: {reserva}")
    return reservas_acomodadas

# Inicializar lista de salas ocupadas (0 representa sala livre, 1 representa sala ocupada)
salas_ocupadas = [[0] * 24 for _ in range(5)]

# Lista de pedidos de reserva
reservas = [
    (9, 10),
    (9, 11),
    (11, 12),
    (10, 11),
    (10, 12),
    (13, 14),
    (13, 14),
    (13, 14),
    (13, 14),
    (13, 14),
    (13, 15)
]

# Acomodar as reservas
reservas_acomodadas = acomodar_reservas(reservas, salas_ocupadas)

# Imprimir as reservas acomodadas
print(reservas_acomodadas)