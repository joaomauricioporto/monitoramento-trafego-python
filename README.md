# Sistema de Monitoramento de Tráfego com Python

Este repositório contém o desenvolvimento de um sistema de monitoramento de tráfego urbano criado em Python. O projeto permite registrar e analisar dados relacionados ao fluxo de veículos em diferentes locais e horários, além de gerar estatísticas e relatórios que ajudam a compreender padrões de trânsito.

O sistema possui uma interface gráfica desenvolvida com CustomTkinter, permitindo a inserção e visualização de dados de forma interativa e organizada.

## Sobre o Projeto

O projeto foi desenvolvido com o objetivo de simular um sistema simples de monitoramento de tráfego urbano. A aplicação permite registrar leituras contendo informações como local, horário, fluxo de veículos, velocidade média e possíveis ocorrências (como acidentes ou obras).

A partir dessas informações, o sistema realiza análises automáticas que ajudam a identificar padrões importantes no trânsito, como horários de pico, média de fluxo de veículos e número de ocorrências registradas.

Além disso, o projeto também foi desenvolvido com foco na prática de organização de código em múltiplos módulos, separando responsabilidades entre interface gráfica, lógica de negócio, estrutura de dados e funções auxiliares.

## Tecnologias Utilizadas

As seguintes tecnologias foram utilizadas no desenvolvimento deste projeto:

- **Python:** Linguagem de programação principal utilizada no desenvolvimento da aplicação.
- **CustomTkinter:** Biblioteca utilizada para a criação da interface gráfica moderna da aplicação.
- **Tkinter:** Biblioteca base utilizada para construção da interface gráfica.
- **Estrutura Modular em Python:** Organização do projeto em diferentes arquivos para separar responsabilidades e melhorar a manutenção do código.

## Estrutura do Repositório

O repositório está organizado da seguinte forma:

- **`gui.py`**: Contém toda a interface gráfica da aplicação.
- **`main.py`**: Versão alternativa do sistema executada via terminal.
- **`models.py`**: Responsável pela estrutura de armazenamento das leituras de tráfego.
- **`services.py`**: Contém as regras de negócio e funções de processamento de dados.
- **`utils.py`**: Funções auxiliares utilizadas para validação de dados e outras operações.

Essa organização permite uma separação clara entre as diferentes responsabilidades do sistema, facilitando futuras melhorias e manutenção do código.

## Como Executar o Projeto

Para executar o projeto em seu ambiente local, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/joaomauricioporto/monitoramento-trafego-python.git
   ```

2. **Navegue até o diretório do projeto:**
   ```bash
   cd monitoramento-trafego-python
   ```

3. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   # venv\Scripts\activate  # Para Windows
   ```

4. **Instale as dependências:**
   ```bash
   pip install customtkinter
   ```

5. **Execute o sistema com interface gráfica:**
   ```bash
   python gui.py
   ```

6. **Opcionalmente, execute a versão via terminal:**
   ```bash
   python main.py
   ```

## Funcionalidades do Sistema

O sistema permite realizar diversas operações relacionadas ao monitoramento de tráfego, incluindo:

- Registro de novas leituras de tráfego
- Consulta de leituras por local
- Consulta de leituras por horário
- Cálculo de média de fluxo de veículos
- Identificação da menor velocidade registrada
- Contagem de ocorrências registradas
- Identificação de horário de pico
- Geração de relatórios detalhados por local

## Possíveis Aplicações

Embora seja um projeto acadêmico e simplificado, sistemas desse tipo podem ser utilizados em cenários reais para:

- Monitoramento de mobilidade urbana
- Análise de padrões de tráfego em cidades
- Identificação de horários críticos de congestionamento
- Apoio a decisões de planejamento urbano
- Avaliação de impacto de obras ou acidentes no trânsito

## Melhorias Futuras

Algumas melhorias que podem ser implementadas futuramente incluem:

- Persistência dos dados em banco de dados ou arquivos JSON
- Geração de gráficos para visualização de dados
- Exportação de relatórios em PDF
- Dashboard com visualização interativa de dados
- Integração com APIs de mobilidade urbana

## Contribuição

Contribuições para o projeto são bem-vindas. Caso tenha sugestões de melhorias, novas funcionalidades ou correções, fique à vontade para abrir uma *issue* ou enviar um *pull request*.

## Autor

- **João Maurício Porto** - [GitHub](https://github.com/joaomauricioporto)
