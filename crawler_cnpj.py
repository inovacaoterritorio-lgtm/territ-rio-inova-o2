name: Atualizar Dados das Startups

on:
  push:
    paths:
      - 'dados_cnpjs.csv'   # Roda automaticamente ao atualizar a lista de CNPJs
  workflow_dispatch:          # Permite disparo manual pelo GitHub

jobs:
  atualizar:
    runs-on: ubuntu-latest

    steps:
    - name: Clonar o repositório
      uses: actions/checkout@v3

    - name: Configurar o Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Instalar dependências
      run: |
        python -m pip install --upgrade pip
        pip install -r scripts/requirements.txt

    - name: Rodar o crawler de CNPJs
      run: |
        python scripts/crawler_cnpj.py

    - name: Salvar alterações e fazer push de volta
      run: |
        git config --global user.name "GitHub Action Bot"
        git config --global user.email "actions@github.com"
        git add startups_data.json
        git diff-index --quiet HEAD || git commit -m "Auto: dados de startups atualizados via BrasilAPI"
        git push
