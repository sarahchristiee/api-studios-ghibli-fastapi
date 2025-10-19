# Estudo FastAPI - API de Filmes do Studio Ghibli

>Este projeto é um estudo sobre FastAPI em Python, onde desenvolvi uma API simples que retorna alguns filmes do Studio Ghibli.

## Funcionalidades

- Listar filmes do Studio Ghibli
- Consultar filmes por id
- Documentação automática da API via Swagger UI

---

## Tutorial: Como executar a API

Siga o passo a passo abaixo para rodar a API localmente:

### 1. Clone o repositório
Abra seu terminal e digite:

```
git clone https://github.com/sarahchristiee/api-studios-ghibli-fastapi.git
cd api-studios-ghibli-fastapi
```

### 2. Crie um ambiente virtual
No terminal do cmd ou do ambiente em que estiver utilizando digite

```
python -m venv venv
.\venv\Scripts\Activate
```

### 3. Instale as depeências
para instalar as depeências e bibliotecas necessárias digite no terminal

```
pip install -r requirements.txt
```

## 4. Execute o servidor
para executar o servidor digite no terminal

```
uvicorn main:app --reload
```

## 5. Acesse a documentação da API

Acesse no navegador de preferência
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

