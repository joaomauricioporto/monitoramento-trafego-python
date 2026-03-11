from services import (
    criar_leitura,
    adicionar_leitura_ao_sistema,
    obter_todas_leituras,
    listar_leituras_por_local,
    listar_leituras_por_horario,
    calcular_media_fluxo_geral,
    encontrar_menor_velocidade_geral,
    contar_ocorrencias_geral,
    encontrar_horario_pico_geral,
    gerar_relatorio_por_local
)
from utils import validar_nao_vazio, validar_horario, validar_numero_positivo, validar_opcao_menu

def exibir_menu():
    print("\n--- MENU DE MONITORAMENTO DE TRÁFEGO ---")
    print("1. Adicionar Nova Leitura")
    print("2. Listar Leituras por Local")
    print("3. Listar Leituras por Horário")
    print("4. Exibir Estatísticas Gerais")
    print("5. Gerar Relatório Detalhado por Local")
    print("6. Sair")
    print("----------------------------------------")

def adicionar_leitura_interativo():
    print("\n--- ADICIONAR NOVA LEITURA ---")
    local = input("Digite o local (ex: Av. Paulista): ")
    while not validar_nao_vazio(local):
        print("Local não pode ser vazio. Tente novamente.")
        local = input("Digite o local (ex: Av. Paulista): ")

    horario = input("Digite o horário (HH:MM, ex: 08:00): ")
    while not validar_horario(horario):
        print("Formato de horário inválido. Use HH:MM. Tente novamente.")
        horario = input("Digite o horário (HH:MM, ex: 08:00): ")

    fluxo_str = input("Digite o fluxo de veículos: ")
    fluxo = validar_numero_positivo(fluxo_str)
    while fluxo is None:
        print("Fluxo inválido. Digite um número positivo. Tente novamente.")
        fluxo_str = input("Digite o fluxo de veículos: ")
        fluxo = validar_numero_positivo(fluxo_str)

    velocidade_str = input("Digite a velocidade média (km/h): ")
    velocidade = validar_numero_positivo(velocidade_str)
    while velocidade is None:
        print("Velocidade inválida. Digite um número positivo. Tente novamente.")
        velocidade_str = input("Digite a velocidade média (km/h): ")
        velocidade = validar_numero_positivo(velocidade_str)

    ocorrencia = input("Digite a ocorrência (opcional, ex: Acidente, Obra, ou deixe vazio): ")
    if not validar_nao_vazio(ocorrencia):
        ocorrencia = "Nenhuma"

    nova_leitura = criar_leitura(local, horario, fluxo, velocidade, ocorrencia)
    if adicionar_leitura_ao_sistema(nova_leitura):
        print("Leitura adicionada com sucesso!")
    else:
        print("Falha ao adicionar leitura. Verifique os dados.")

def listar_por_local_interativo():
    print("\n--- LISTAR LEITURAS POR LOCAL ---")
    local_busca = input("Digite o local para buscar: ")
    while not validar_nao_vazio(local_busca):
        print("Local não pode ser vazio. Tente novamente.")
        local_busca = input("Digite o local para buscar: ")

    leituras = listar_leituras_por_local(local_busca)
    if leituras:
        print(f"\nLeituras encontradas para {local_busca}:")
        for l in leituras:
            print(f"  Horário: {l['horario']}, Fluxo: {l['fluxo']}, Velocidade: {l['velocidade']:.2f} km/h, Ocorrência: {l['ocorrencia']}")
    else:
        print(f"Nenhuma leitura encontrada para o local '{local_busca}'.")

def listar_por_horario_interativo():
    print("\n--- LISTAR LEITURAS POR HORÁRIO ---")
    horario_busca = input("Digite o horário para buscar (HH:MM): ")
    while not validar_horario(horario_busca):
        print("Formato de horário inválido. Use HH:MM. Tente novamente.")
        horario_busca = input("Digite o horário para buscar (HH:MM): ")

    leituras = listar_leituras_por_horario(horario_busca)
    if leituras:
        print(f"\nLeituras encontradas para {horario_busca}:")
        for l in leituras:
            print(f"  Local: {l['local']}, Fluxo: {l['fluxo']}, Velocidade: {l['velocidade']:.2f} km/h, Ocorrência: {l['ocorrencia']}")
    else:
        print(f"Nenhuma leitura encontrada para o horário '{horario_busca}'.")

def exibir_estatisticas_interativo():
    print("\n--- ESTATÍSTICAS GERAIS ---")
    todas_leituras = obter_todas_leituras()
    if not todas_leituras:
        print("Não há leituras para gerar estatísticas.")
        return

    media_fluxo = calcular_media_fluxo_geral(todas_leituras)
    menor_velocidade = encontrar_menor_velocidade_geral(todas_leituras)
    total_ocorrencias = contar_ocorrencias_geral(todas_leituras)
    horario_pico = encontrar_horario_pico_geral(todas_leituras)

    print(f"Média de Fluxo Geral: {media_fluxo:.2f} veículos")
    print(f"Menor Velocidade Média Registrada: {menor_velocidade:.2f} km/h")
    print(f"Total de Ocorrências: {total_ocorrencias}")
    print(f"Horário de Pico Geral: {horario_pico}")

def gerar_relatorio_interativo():
    print("\n--- GERAR RELATÓRIO DETALHADO POR LOCAL ---")
    todas_leituras = obter_todas_leituras()
    if not todas_leituras:
        print("Não há leituras para gerar o relatório.")
        return
    
    relatorio = gerar_relatorio_por_local(todas_leituras)
    print(relatorio)

def main():
    while True:
        exibir_menu()
        opcao_str = input("Escolha uma opção: ")
        opcao = validar_opcao_menu(opcao_str, [1, 2, 3, 4, 5, 6])

        if opcao == 1:
            adicionar_leitura_interativo()
        elif opcao == 2:
            listar_por_local_interativo()
        elif opcao == 3:
            listar_por_horario_interativo()
        elif opcao == 4:
            exibir_estatisticas_interativo()
        elif opcao == 5:
            gerar_relatorio_interativo()
        elif opcao == 6:
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 6.")

if __name__ == "__main__":
    main()