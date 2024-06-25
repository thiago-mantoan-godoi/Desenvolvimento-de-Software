import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
from genetic_algorithm.main import main as run_genetic_algorithm

class OptimizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Otimização de Fabricação de Chicotes Elétricos")
        
        # Variáveis de entrada
        self.parametros = []

        # Criar layout
        self.create_widgets()

    def create_widgets(self):
        # Adicionar campos de entrada para os parâmetros
        for i in range(5):  # Exemplo com 5 parâmetros
            ttk.Label(self.root, text=f"Parâmetro {i+1}:").grid(row=i, column=0, padx=10, pady=5)
            entry = ttk.Entry(self.root, width=10)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.parametros.append(entry)
        
        # Botão para iniciar a otimização
        self.start_button = ttk.Button(self.root, text="Iniciar Otimização", command=self.start_optimization)
        self.start_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Área para exibir resultados
        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def start_optimization(self):
        # Obter os parâmetros de entrada e iniciar a otimização em uma nova thread
        try:
            parametros = [float(entry.get()) for entry in self.parametros]
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para todos os parâmetros.")
            return
        
        self.results_text.insert(tk.END, "Iniciando otimização...\n")

        thread = Thread(target=self.run_optimization, args=(parametros,))
        thread.start()

    def run_optimization(self, parametros):
        # Executar o algoritmo genético com os parâmetros fornecidos
        best_solution = run_genetic_algorithm(parametros)
        
        self.results_text.insert(tk.END, f"Melhor solução encontrada: {best_solution}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = OptimizationApp(root)
    root.mainloop()
