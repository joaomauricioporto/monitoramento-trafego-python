from models import leituras_de_trafego
from utils import validar_horario, validar_numero_positivo, validar_nao_vazio
import datetime


def criar_leitura(local, horario, fluxo, velocidade, ocorrencia="Nenhuma"):
    if not validar_nao_vazio(local):
        print("Erro: Local não pode ser vazio.")
        return None
    if not validar_horario(horario):
        print("Erro: Horário inválido. Use HH:MM.")
        return None
    if validar_numero_positivo(str(fluxo)) is None:
        print("Erro: Fluxo deve ser um número positivo.")
        return None
    if validar_numero_positivo(str(velocidade)) is None:
        print("Erro: Velocidade deve ser um número positivo.")
        return None

    leitura = {
        "local": local,
        "horario": horario,
        "fluxo": fluxo,
        "velocidade": velocidade,
        "ocorrencia": ocorrencia
    }
    return leitura

def adicionar_leitura_ao_sistema(leitura):
    if leitura:
        leituras_de_trafego.append(leitura)
        return True
    return False

def obter_todas_leituras():
    return leituras_de_trafego


def listar_leituras_por_local(local_procurado):
    leituras_filtradas = []
    for leitura in leituras_de_trafego:
        if leitura["local"].lower() == local_procurado.lower():
            leituras_filtradas.append(leitura)
    return leituras_filtradas

def listar_leituras_por_horario(horario_procurado):
    leituras_filtradas = []
    for leitura in leituras_de_trafego:
        if leitura["horario"] == horario_procurado:
            leituras_filtradas.append(leitura)
    return leituras_filtradas


def _classificar_transito(fluxo):
    if fluxo < 50:
        return "Leve"
    elif 50 <= fluxo <= 150:
        return "Moderado"
    else:
        return "Intenso"


def calcular_media_fluxo_geral(leituras):
    if not leituras:
        return 0.0
    total_fluxo = 0
    for leitura in leituras:
        total_fluxo += leitura["fluxo"]
    return total_fluxo / len(leituras)

def encontrar_menor_velocidade_geral(leituras):
    if not leituras:
        return 0.0
    menor_velocidade = leituras[0]["velocidade"]
    for leitura in leituras:
        if leitura["velocidade"] < menor_velocidade:
            menor_velocidade = leitura["velocidade"]
    return menor_velocidade

def contar_ocorrencias_geral(leituras):
    total_ocorrencias = 0
    for leitura in leituras:
        if leitura["ocorrencia"] != "Nenhuma":
            total_ocorrencias += 1
    return total_ocorrencias

def encontrar_horario_pico_geral(leituras):
    if not leituras:
        return "N/A"
    fluxo_por_horario = {}
    for leitura in leituras:
        hora = leitura["horario"]
        if hora in fluxo_por_horario:
            fluxo_por_horario[hora] += leitura["fluxo"]
        else:
            fluxo_por_horario[hora] = leitura["fluxo"]
    
    if not fluxo_por_horario:
        return "N/A"
    
    horario_pico = "N/A"
    max_fluxo = -1
    for hora, fluxo in fluxo_por_horario.items():
        if fluxo > max_fluxo:
            max_fluxo = fluxo
            horario_pico = hora
    return horario_pico


def _gerar_dados_agregados_por_local(leituras):
    dados_agregados = {}
    for r in leituras:
        local = r["local"]
        if local not in dados_agregados:
            dados_agregados[local] = {
                "fluxo_total": 0,
                "velocidade_total": 0,
                "contagem": 0,
                "ocorrencias": 0,
                "fluxo_por_horario_local": {}
            }
        
        dados_agregados[local]["fluxo_total"] += r["fluxo"]
        dados_agregados[local]["velocidade_total"] += r["velocidade"]
        dados_agregados[local]["contagem"] += 1
        if r["ocorrencia"] != "Nenhuma":
            dados_agregados[local]["ocorrencias"] += 1
        
        hora = r["horario"]
        fluxo_hora_local = dados_agregados[local]["fluxo_por_horario_local"]
        if hora in fluxo_hora_local:
            fluxo_hora_local[hora] += r["fluxo"]
        else:
            fluxo_hora_local[hora] = r["fluxo"]
    return dados_agregados

def calcular_media_fluxo_local(dados_local):
    if dados_local["contagem"] == 0:
        return 0.0
    return dados_local["fluxo_total"] / dados_local["contagem"]

def calcular_media_velocidade_local(dados_local):
    if dados_local["contagem"] == 0:
        return 0.0
    return dados_local["velocidade_total"] / dados_local["contagem"]

def contar_ocorrencias_local(dados_local):
    return dados_local["ocorrencias"]

def encontrar_horario_pico_local(dados_local):
    fluxo_por_horario = dados_local["fluxo_por_horario_local"]
    if not fluxo_por_horario:
        return "N/A"
    
    horario_pico = "N/A"
    max_fluxo = -1
    for hora, fluxo in fluxo_por_horario.items():
        if fluxo > max_fluxo:
            max_fluxo = fluxo
            horario_pico = hora
    return horario_pico

def gerar_relatorio_por_local(leituras):
    if not leituras:
        return "Não há leituras para gerar o relatório.\n"

    dados_agregados = _gerar_dados_agregados_por_local(leituras)
    relatorio_str = "\n--- Relatório Detalhado por Local ---\n"

    for local, dados in dados_agregados.items():
        media_fluxo = calcular_media_fluxo_local(dados)
        media_velocidade = calcular_media_velocidade_local(dados)
        classificacao = _classificar_transito(media_fluxo)
        ocorrencias = contar_ocorrencias_local(dados)
        horario_pico = encontrar_horario_pico_local(dados)

        relatorio_str += f"\nLocal: {local}\n"
        relatorio_str += f"  - Média de Fluxo: {media_fluxo:.2f} veículos\n"
        relatorio_str += f"  - Média de Velocidade: {media_velocidade:.2f} km/h\n"
        relatorio_str += f"  - Classificação do Trânsito: {classificacao}\n"
        relatorio_str += f"  - Total de Ocorrências: {ocorrencias}\n"
        relatorio_str += f"  - Horário de Pico do Local: {horario_pico} (com {dados['fluxo_por_horario_local'].get(horario_pico, 0)} veículos)\n"
    
    return relatorio_str