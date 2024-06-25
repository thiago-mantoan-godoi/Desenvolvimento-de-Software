### README.md

# Otimização de Parâmetros de Fabricação de Chicotes Elétricos

Este projeto utiliza algoritmos genéticos para otimizar os parâmetros de fabricação de chicotes elétricos. A otimização é baseada em uma função de fitness que considera critérios como custo, qualidade e tempo de produção.

## Estrutura do Projeto

- `main.py`: Ponto de entrada do software.
- `ga.py`: Implementação do algoritmo genético.
- `fitness.py`: Definição das funções de fitness.
- `ui.py`: Interface do usuário.
- `requirements.txt`: Dependências do projeto.

## Funcionalidades

- Otimização de parâmetros utilizando algoritmos genéticos.
- Função de fitness considerando custo, qualidade e tempo de produção.
- Interface gráfica para facilitar a interação do usuário.
- Visualização dos resultados obtidos após a execução do algoritmo.

## Requisitos

- Python 3.x
- Bibliotecas listadas em `requirements.txt`

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/thiago-mantoan-godoi/Desenvolvimento-de-Software.git
cd otimizacao-chicotes-eletricos
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Execute o software com o seguinte comando:

```bash
python main.py
```

## Uso

1. Defina o número de gerações e o tamanho da população na interface gráfica.
2. Clique no botão "Executar" para iniciar o algoritmo genético.
3. Os resultados serão exibidos em uma nova janela, mostrando o melhor indivíduo encontrado e suas características.

## Estrutura do Código

### `fitness.py`

Define as funções de cálculo de custo, qualidade e tempo de produção, além da função de fitness que combina esses critérios.

### `ga.py`

Configura e executa o algoritmo genético utilizando a biblioteca `deap`.

### `ui.py`

Implementa a interface gráfica usando `tkinter`, permitindo ao usuário definir parâmetros e visualizar os resultados.

### `main.py`

Ponto de entrada do software que inicializa a interface gráfica.

## Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para a branch (`git push origin feature/nova-feature`).
5. Crie um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Para mais informações, sinta-se à vontade para abrir uma issue ou enviar um e-mail para [godoi.thiago@yahoo.com.br(mailto:seu-email@dominio.com).