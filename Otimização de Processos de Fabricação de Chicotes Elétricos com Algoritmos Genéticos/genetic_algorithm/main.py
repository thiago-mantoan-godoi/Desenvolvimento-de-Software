import random
from deap import base, creator, tools, algorithms

# Definição do problema e criação dos tipos de indivíduos e fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Configuração da Toolbox para o algoritmo genético
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0, 10)  # Exemplo: variáveis entre 0 e 10
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=5)  # 5 variáveis no indivíduo
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Função de avaliação (fitness function)
def evaluate(individual):
    # Exemplo simples: minimizar a soma das variáveis do indivíduo
    return sum(individual),

toolbox.register("mate", tools.cxBlend, alpha=0.5)  # Operador de cruzamento
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)  # Operador de mutação
toolbox.register("select", tools.selTournament, tournsize=3)  # Operador de seleção

def main(parametros):
    population = toolbox.population(n=50)  # População inicial com 50 indivíduos
    ngen = 100  # Número de gerações
    cxpb = 0.5  # Probabilidade de cruzamento
    mutpb = 0.2  # Probabilidade de mutação
    
    # Registrar a função de avaliação na Toolbox
    toolbox.register("evaluate", evaluate)

    # Executar o algoritmo genético
    algorithms.eaSimple(population, toolbox, cxpb, mutpb, ngen, verbose=True)
    
    # Retornar o melhor indivíduo encontrado
    best_individual = tools.selBest(population, k=1)[0]
    return best_individual

if __name__ == "__main__":
    # Exemplo de como rodar o algoritmo diretamente
    # parametros = [1.0, 2.0, 3.0, 4.0, 5.0]
    # best_solution = main(parametros)
    # print("Melhor solução encontrada:", best_solution)
    pass  # Se rodar main() diretamente aqui, não irá passar parametros
