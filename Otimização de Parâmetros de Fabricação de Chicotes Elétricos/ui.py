import tkinter as tk
from tkinter import ttk
from ga import configure_ga, run_ga
from fitness import calculate_cost, calculate_quality, calculate_production_time

class GAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Otimização de Chicotes Elétricos")
        
        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.gen_label = ttk.Label(self.frame, text="Número de Gerações:")
        self.gen_label.grid(row=0, column=0, sticky=tk.W)
        self.gen_entry = ttk.Entry(self.frame)
        self.gen_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        self.pop_label = ttk.Label(self.frame, text="Tamanho da População:")
        self.pop_label.grid(row=1, column=0, sticky=tk.W)
        self.pop_entry = ttk.Entry(self.frame)
        self.pop_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))
        
        self.run_button = ttk.Button(self.frame, text="Executar", command=self.run_ga)
        self.run_button.grid(row=2, column=0, columnspan=2)

    def run_ga(self):
        n_gen = int(self.gen_entry.get())
        n_pop = int(self.pop_entry.get())
        
        toolbox = configure_ga()
        pop, stats, hof = run_ga(toolbox, n_gen, n_pop)
        
        best_individual = hof[0]
        
        result = f"Melhor indivíduo: {best_individual}\n"
        result += f"Fitness: {best_individual.fitness.values[0]}\n"
        result += f"Custo: {calculate_cost(best_individual)}\n"
        result += f"Qualidade: {calculate_quality(best_individual)}\n"
        result += f"Tempo de Produção: {calculate_production_time(best_individual)}\n"
        
        self.show_results(result)

    def show_results(self, result):
        result_window = tk.Toplevel(self.root)
        result_window.title("Resultados")
        
        result_text = tk.Text(result_window, wrap=tk.WORD)
        result_text.insert(tk.END, result)
        result_text.grid(row=0, column=0, padx=10, pady=10)
        
        ok_button = ttk.Button(result_window, text="OK", command=result_window.destroy)
        ok_button.grid(row=1, column=0, pady=10)

def main():
    root = tk.Tk()
    app = GAApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
