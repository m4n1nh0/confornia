# ConfornIA

ConfornIA é uma aplicação web que fornece uma interface amigável para gerenciar perguntas e processos de auditoria. É construído usando Python e alavanca bibliotecas poderosas como FastAPI, SQLAlchemy e PostgreSQL para entregar uma solução robusta e escalável.

## Começando

### Pré-requisitos:

- Docker instalado e em execução (https://docs.docker.com/engine/install/)
- Docker Compose instalado (https://docs.docker.com/compose/install/)

### Clone o Repositório:

```bash
git clone https://github.com/your-username/confornia.git
cd confornia
```

Construa e Execute os Containers:

```bash
docker-compose up -d
```

Isso construirá as imagens Docker para o banco de dados PostgreSQL (confpostgres) e o aplicativo backend ConfornIA (confornia_app), criará e conectá-los à rede confornia_net e iniciá-los em segundo plano.

### Acesse a Aplicação:

Depois que os containers estiverem em execução, você poderá acessar a API backend ConfornIA em [http://localhost:8000](http://localhost:8000). A URL exata pode variar dependendo da sua configuração de desenvolvimento.

## Estrutura do Projeto

O projeto está organizado em um layout de diretório bem estruturado:

- `main.py`: O ponto de entrada da aplicação, inicializando a instância FastAPI, configurando o middleware e definindo rotas de API.
- `settings`: Um diretório que abriga arquivos de configuração relacionados à configuração do FastAPI e da infraestrutura:
  - `fastapi_middlewares.py`: Define funções de middleware personalizadas para o aplicativo FastAPI.
  - `infra_environment.py`: Fornece acesso às variáveis ​​de ambiente usadas pelo aplicativo.
  - `openapi.py`: Lida com a geração da especificação OpenAPI para a API.
- `routes`: Um diretório que contém módulos que definem rotas de API agrupadas por funcionalidade:
  - `questions.py`: Define rotas relacionadas ao gerenciamento de perguntas dentro do aplicativo.
  - `auditoria.py`: Define rotas relacionadas à funcionalidade de auditoria.

## Dependências Essenciais

O aplicativo depende de um conjunto cuidadosamente selecionado de bibliotecas para entregar suas funcionalidades:

- **FastAPI**: Uma estrutura de alto desempenho e focada na web para construir APIs modernas.
- **SQLAlchemy**: Um mapeador objeto-relacional (ORM) que simplifica a interação com bancos de dados relacionais como PostgreSQL.
- **PostgreSQL**: Um sistema de gerenciamento de banco de dados relacional (RDBMS) de código aberto robusto e escalável.
- **Dependências Adicionais**: Uma variedade de bibliotecas que fornecem funcionalidades essenciais como validação de dados, serialização e recursos do cliente HTTP.

## Variáveis ​​de Ambiente (Opcional)

O arquivo `docker-compose.yml` define algumas variáveis ​​de ambiente para o serviço `confornia_app`. Você pode personalizar esses valores de acordo com suas necessidades:

- `ALLOWED_HOST`: Lista separada por vírgulas de nomes de host e portas permitidos para o serviço de back-end (o padrão permite localhost e o domínio fornecido).
- `ALLOW_ORIGINS`: Lista separada por vírgulas de origens permitidas para CORS (o padrão permite localhost e o domínio fornecido).

## Persistência de Dados

O arquivo `docker-compose.yml` define um volume denominado `pgdata` que persiste o diretório de dados do banco de dados PostgreSQL (`/var/lib/postgresql/data`). Isso garante que seus dados de banco de dados não sejam perdidos quando os containers forem parados ou reiniciados.

## Fluxo de Trabalho de Desenvolvimento

Para fazer alterações no código sem parar e reiniciar os containers, você pode usar o mapeamento de volume:

```bash
- .:/code  # Monta o diretório atual como /code dentro do container
```

Isso permite que você edite seu código localmente e as alterações serão refletidas no container em execução automaticamente.

### Parar os Containers

Para parar os containers com elegância:

```bash
docker-compose down
```

## Conclusão

ConfornIA oferece uma plataforma poderosa e amigável para gerenciar perguntas e processos de auditoria, aproveitando tecnologias modernas e uma base de código bem estruturada. Com seus recursos abrangentes e facilidade de uso, ConfornIA é um ativo para organizações que buscam agilizar seus fluxos de trabalho de gerenciamento de perguntas e auditoria.
