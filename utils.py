import datetime

def validar_nao_vazio(texto):
    return bool(texto.strip())

def validar_horario(horario):
    try:
        datetime.datetime.strptime(horario, "%H:%M")
        return True
    except ValueError:
        return False

def validar_numero_positivo(numero_str):
    try:
        numero = float(numero_str)
        if numero >= 0:
            return numero
        else:
            return None
    except ValueError:
        return None

def validar_opcao_menu(opcao_str, opcoes_validas):
    try:
        opcao = int(opcao_str)
        if opcao in opcoes_validas:
            return opcao
        else:
            return None
    except ValueError:
        return None