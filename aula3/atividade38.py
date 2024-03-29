def calcular_horario_termino(hora_inicio, minuto_inicio, segundo_inicio, duracao_segundos):

    total_segundos_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
    
    total_segundos_termino = total_segundos_inicio + duracao_segundos
    
    hora_termino = total_segundos_termino // 3600
    total_segundos_termino %= 3600
    minuto_termino = total_segundos_termino // 60
    segundo_termino = total_segundos_termino % 60
    
    return hora_termino, minuto_termino, segundo_termino

def main():

    hora_inicio = int(input("Digite a hora de início (0-23): "))
    minuto_inicio = int(input("Digite o minuto de início (0-59): "))
    segundo_inicio = int(input("Digite o segundo de início (0-59): "))

    duracao_segundos = int(input("Digite a duração em segundos: "))

    hora_termino, minuto_termino, segundo_termino = calcular_horario_termino(hora_inicio, minuto_inicio, segundo_inicio, duracao_segundos)

    print("Horário de término:", hora_termino, "horas,", minuto_termino, "minutos e", segundo_termino, "segundos.")

if __name__ == "__main__":
    main()