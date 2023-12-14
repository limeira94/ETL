# ETL Carga de Dados Excel

Este é um script Python para extrair dados de um arquivo Excel e carregá-los em um banco de dados Oracle.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- cx_Oracle
- pandas
- dotenv
- Oracle Client (para conectar-se ao banco de dados Oracle)

## Configuração

1. Clone o repositório e navegue até o diretório do projeto:
```
$ git clone <URL_DO_REPOSITORIO>
$ cd <NOME_DO_DIRETORIO>
```

2. Instale as dependências usando o gerenciador de pacotes do Python (pip):


3. Crie um arquivo `.env` na raiz do projeto e defina as seguintes variáveis de ambiente:
```DB_USERNAME=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=seu_host:porta/servico
```

## Uso

1. Coloque o arquivo Excel que contém os dados a serem carregados em um diretório acessível pelo script. Certifique-se de fornecer o caminho completo do arquivo.

2. Abra o arquivo `etl.py` e modifique a variável `fp` com o caminho completo do arquivo Excel:

```python
fp = '/caminho/para/o/seu/arquivo.xlsx'

$ python etl.py
```
