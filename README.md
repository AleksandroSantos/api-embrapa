# Projeto de Ingestão de Dados da Embrapa

## Descrição do Projeto

Este projeto realiza a ingestão de dados das abas Produção, Processamento, Comercialização, Importação e Exportação do site da Embrapa. Os dados são armazenados em arquivos CSV e disponibilizados através de uma API REST em Python. O projeto inclui testes unitários e autenticação JWT para garantir a segurança das requisições.

## Estrutura do Projeto

    api-embrapa/
    ├── api/
    │   ├── __init__.py
    │   ├── app.py
    │   ├── models.py
    │   └── security.py
    ├── config/
    │   └── config.py
    ├── data/
    │   ├── processed_data/
    │   └── raw_data/
    │       ├── Comercialização.csv
    │       ├── Exportação.csv
    │       ├── Importação.csv
    │       ├── Processamento.csv
    │       └── Produção.csv
    ├── notebooks/
    │   └── exploratory_notebook.ipynb
    ├── scrapers/
    │   ├── __init__.py
    │   └── main.py
    │   ├── scraper.py
    ├── tests/
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── test_scraper.py
    ├── utils/
    │   └── utils.py
    ├── .gitignore
    ├── requirements.txt
    └── README.md



## Requisitos

- Python 3.x
- virtualenv (opcional, mas recomendado)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/AleksandroSantos/api-embrapa.git
    cd api-embrapa
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```


## Ingestão de Dados
Os dados são ingeridos usando scripts de scraping. Os scripts estão localizados na pasta scrapers/.

Exemplo de Uso do Scraper

```bash
python scrapers/main.py 
```

### Configurar os Arquivos CSV
Os dados de vitivinicultura são armazenados em arquivos CSV na pasta data/. Certifique-se de ter os arquivos producao.csv, processamento.csv, comercializacao.csv, importacao.csv e exportacao.csv nessa pasta.


## Endpoints da API

A API possui os seguintes endpoints:

### Autenticação
- Login
    - URL: `/token`
    - Método: `POST`
    - Descrição: Autentica o usuário e retorna um token JWT.
    - Exemplo de Requisição:
    ```json
        {
            "username": "user",
            "password": "password"
        }
    ```
    - Exemplo de Resposta:
    ```json
        {
            "access_token": "seu-jwt-token",
            "token_type": "bearer"
        }
    ```
### Dados

- Obter Dados de Produção
    - URL: `/producao`
    - Método: `GET`
    - Descrição: Retorna os dados de produção.
    - Exemplo de Requisição:
        ```
            GET /producao
            Authorization: Bearer seu-jwt-token
        ```
    - Exemplo de Resposta:
        ```json
            {
                "produto": "VINHO DE MESA",
                "quantidade": "217.208.604",
                "ano": 1970
            }
        ```
- Obter Dados de Processamento
    - URL: `/processamento`
    - Método: `GET`
    - Descrição: Retorna os dados de processamento.
    - Exemplo de Requisição:
        ```
            GET /processamento
            Authorization: Bearer seu-jwt-token
        ```
    - Exemplo de Resposta:
        ```json
            {
                "cultivar": "TINTAS",
                "quantidade": "10.448.228",
                "ano": 1970,
                "opcao": "Viníferas",
                "sem_definicao": "-"
            }
        ```
- Obter Dados de Comercialização
    - URL: `/comercializacao`
    - Método: `GET`
    - Descrição: Retorna os dados de comercialização.
    - Exemplo de Requisição:
        ```
            GET /comercializacao
            Authorization: Bearer seu-jwt-token
        ```
    - Exemplo de Resposta:
        ```json
            {
                "produto": "VINHO DE MESA",
                "quantidade": "98.327.606",
                "ano": 1970
            }
        ```
    
- Obter Dados de Importação
    - URL: `/importacao`
    - Método: `GET`
    - Descrição: Retorna os dados de importação.
    - Exemplo de Requisição:
        ```
            GET /importacao
            Authorization: Bearer seu-jwt-token
        ```
    - Exemplo de Resposta:
        ```json
            {
                "países": "Africa do Sul",
                "quantidade": "-",
                "valor": "-",
                "ano": 1970,
                "opcao": "Vinhos de mesa"
            }
        ```
    
- Obter Dados de Exportação
    - URL: `/exportacao`
    - Método: `GET`
    - Descrição: Retorna os dados de exportação.
    - Exemplo de Requisição:
        ```
            GET /exportacao
            Authorization: Bearer seu-jwt-token
        ```
    - Exemplo de Resposta:
        ```json
            {
                "países": "Afeganistão",
                "quantidade": "-",
                "valor": "-",
                "ano": 1970,
                "opcao": "Vinhos de mesa"
            }
        ```


### Executando o Projeto

Para iniciar a aplicação, execute o seguinte comando:

```bash
python api/app.py
```
A API estará disponível em http://127.0.0.1:8000.

### Testes

Os testes estão localizados na pasta tests/.
Para executar os testes unitários, utilize o comando:

```bash
python -m pytest
```

### Documentação da API
A documentação da API estará disponível em http://127.0.0.1:8000/docs.

