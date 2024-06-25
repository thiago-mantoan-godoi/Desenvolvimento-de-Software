## TaskHub

Plataforma Web para Monitoramento de Tarefas em Projetos.

### Documentação

Visão geral e documentação do projeto.

* [Documento de Visão](docs/doc-visao.md)

### Desenvolvimento

Passos para configurar o ambiente de desenvolvimento.

#### Criar Ambiente Virtual (Opcional)

```bash
python -m venv env
```

#### Instalar Dependências do Projeto

```bash
cd TaskHub
pip install -r requirements.txt
```

#### Executar Migrações

```bash
cd TaskHub/TaskHub/tasks
python manage.py makemigrations
python manage.py migrate
```

#### Iniciar Servidor de Desenvolvimento

```bash
python manage.py runserver
```

#### Configurar o Interpretador Python no VSCode

Pressione Ctrl + Shift + P e selecione "Python: Select Interpreter",
    escolha o interpretador adequado na lista.

![VSCode](https://i.stack.imgur.com/XQEku.gif)

Fonte: [Stack Overflow](https://stackoverflow.com/questions/53939751/pylint-unresolved-import-error-in-visual-studio-code)

##### Avisos de Importação Não Resolvida

Para resolver problemas de importação não resolvida com **Pylance - VSCode**, adicione caminhos extras para análise:

```json
{
    "python.analysis.extraPaths": ["./sources"]
}
```

Fonte: [PyLance](https://github.com/microsoft/pylance-release/blob/master/TROUBLESHOOTING.md#unresolved-import-warnings)