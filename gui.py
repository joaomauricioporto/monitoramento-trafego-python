import customtkinter as ctk
from tkinter import messagebox


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
from utils import validar_nao_vazio, validar_horario, validar_numero_positivo


class AdicionarLeituraFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(self, text="ADICIONAR NOVA LEITURA", font=ctk.CTkFont(size=16, weight="bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ctk.CTkLabel(self, text="Local:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.local_entry = ctk.CTkEntry(self, placeholder_text="Ex: Av. Paulista")
        self.local_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self, text="Horário (HH:MM):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.horario_entry = ctk.CTkEntry(self, placeholder_text="Ex: 08:00")
        self.horario_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self, text="Fluxo de Veículos:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.fluxo_entry = ctk.CTkEntry(self, placeholder_text="Ex: 120")
        self.fluxo_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self, text="Velocidade Média (km/h):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.velocidade_entry = ctk.CTkEntry(self, placeholder_text="Ex: 30.5")
        self.velocidade_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self, text="Ocorrência (opcional):").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.ocorrencia_entry = ctk.CTkEntry(self, placeholder_text="Ex: Acidente, Obra")
        self.ocorrencia_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkButton(self, text="Adicionar Leitura", command=self.adicionar_leitura_action).grid(row=6, column=0, columnspan=2, pady=20)

    def adicionar_leitura_action(self):
        local = self.local_entry.get()
        horario = self.horario_entry.get()
        fluxo_str = self.fluxo_entry.get()
        velocidade_str = self.velocidade_entry.get()
        ocorrencia = self.ocorrencia_entry.get() or "Nenhuma"

        if not validar_nao_vazio(local) or not validar_horario(horario):
            messagebox.showerror("Erro", "Verifique o Local e o Horário (HH:MM).")
            return
        
        fluxo = validar_numero_positivo(fluxo_str)
        velocidade = validar_numero_positivo(velocidade_str)

        if fluxo is None or velocidade is None:
            messagebox.showerror("Erro", "Fluxo e Velocidade devem ser números positivos.")
            return

        nova_leitura = criar_leitura(local, horario, fluxo, velocidade, ocorrencia)
        if adicionar_leitura_ao_sistema(nova_leitura):
            messagebox.showinfo("Sucesso", "Leitura adicionada!")
            self.local_entry.delete(0, ctk.END)
            self.horario_entry.delete(0, ctk.END)
            self.fluxo_entry.delete(0, ctk.END)
            self.velocidade_entry.delete(0, ctk.END)
            self.ocorrencia_entry.delete(0, ctk.END)

class ListarLeiturasFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self, text="LISTAR LEITURAS", font=ctk.CTkFont(size=16, weight="bold")).grid(row=0, column=0, pady=10)
        
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.tabview.add("Por Local")
        self.tabview.add("Por Horário")

        # Aba Local
        self.local_entry = ctk.CTkEntry(self.tabview.tab("Por Local"), placeholder_text="Local")
        self.local_entry.pack(pady=5)
        ctk.CTkButton(self.tabview.tab("Por Local"), text="Buscar", command=self.buscar_local).pack(pady=5)
        self.txt_local = ctk.CTkTextbox(self.tabview.tab("Por Local"), height=150)
        self.txt_local.pack(fill="both", expand=True, padx=10, pady=10)

        # Aba Horário
        self.hora_entry = ctk.CTkEntry(self.tabview.tab("Por Horário"), placeholder_text="HH:MM")
        self.hora_entry.pack(pady=5)
        ctk.CTkButton(self.tabview.tab("Por Horário"), text="Buscar", command=self.buscar_hora).pack(pady=5)
        self.txt_hora = ctk.CTkTextbox(self.tabview.tab("Por Horário"), height=150)
        self.txt_hora.pack(fill="both", expand=True, padx=10, pady=10)

    def buscar_local(self):
        res = listar_leituras_por_local(self.local_entry.get())
        self.txt_local.delete("1.0", ctk.END)
        for l in res: self.txt_local.insert(ctk.END, f"{l['horario']} - {l['fluxo']} veíc. - {l['velocidade']}km/h\n")

    def buscar_hora(self):
        res = listar_leituras_por_horario(self.hora_entry.get())
        self.txt_hora.delete("1.0", ctk.END)
        for l in res: self.txt_hora.insert(ctk.END, f"{l['local']} - {l['fluxo']} veíc. - {l['velocidade']}km/h\n")

class EstatisticasFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="ESTATÍSTICAS GERAIS", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        self.txt = ctk.CTkTextbox(self, height=200)
        self.txt.pack(fill="both", expand=True, padx=20, pady=10)
        ctk.CTkButton(self, text="Atualizar", command=self.atualizar).pack(pady=10)
        self.atualizar()

    def atualizar(self):
        leituras = obter_todas_leituras()
        self.txt.delete("1.0", ctk.END)
        if not leituras:
            self.txt.insert("1.0", "Sem dados.")
            return
        info = f"Média Fluxo: {calcular_media_fluxo_geral(leituras):.2f}\n"
        info += f"Menor Vel: {encontrar_menor_velocidade_geral(leituras):.2f}\n"
        info += f"Pico: {encontrar_horario_pico_geral(leituras)}"
        self.txt.insert("1.0", info)

class RelatorioDetalhadoFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="RELATÓRIO POR LOCAL", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        self.txt = ctk.CTkTextbox(self, height=300)
        self.txt.pack(fill="both", expand=True, padx=20, pady=10)
        ctk.CTkButton(self, text="Gerar", command=self.gerar).pack(pady=10)
        self.gerar()

    def gerar(self):
        self.txt.delete("1.0", ctk.END)
        self.txt.insert("1.0", gerar_relatorio_por_local(obter_todas_leituras()))

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Monitoramento de Tráfego")
        self.geometry("800x550")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu = ctk.CTkFrame(self, width=150)
        self.menu.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkButton(self.menu, text="Adicionar", command=lambda: self.mudar_tela(AdicionarLeituraFrame)).pack(pady=10, padx=10)
        ctk.CTkButton(self.menu, text="Listar", command=lambda: self.mudar_tela(ListarLeiturasFrame)).pack(pady=10, padx=10)
        ctk.CTkButton(self.menu, text="Estatísticas", command=lambda: self.mudar_tela(EstatisticasFrame)).pack(pady=10, padx=10)
        ctk.CTkButton(self.menu, text="Relatório", command=lambda: self.mudar_tela(RelatorioDetalhadoFrame)).pack(pady=10, padx=10)

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.tela_atual = None
        self.mudar_tela(AdicionarLeituraFrame)

    def mudar_tela(self, classe_frame):
        if self.tela_atual: self.tela_atual.destroy()
        self.tela_atual = classe_frame(self.container)
        self.tela_atual.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()