<p align="center">

  <h3 align="center">eWallet</h3>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Lincense&message=GPL&color=0000ff" alt="License" />
</p>

<p align="center">
    Esta API foi criada para ser usada no eWallet (um website financeiro) desenvolvido para a pós graduação de Engenharia de Software da PUC-Rio.
    <br />
    <a href="README.md">🇺🇸Inglês</a>
    ·
    <a href="README-pt.md">🇧🇷Português</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## 🗂 Tabela de Conteúdos

* [Sobre o projeto](#book-sobre-o-projeto)
  * [Tecnologias](#computer-technologies)
* [Instalação](#bricks-instalaçao)
  * [Pré-requisitos](#construction-pre-requisitos)
  * [Back-end](#file_cabinet-back-end)
    * [Instalando Dependências](#construction-instalando-dependencias)
    <!-- * [Setting Back-end](#wrench-setting-back-end) -->
    * [Rodando Back-end](#arrow_forward-rodando-back-end)
* [Licença](#page_facing_up-licença)
* [Autora](#woman_technologist-autora)

## :book: Sobre o projeto

Esta é a API do website financeiro eWallet desenvolvido para obter nota na PUC-Rio.

Link para acessar o front-end do projeto: [eWallet-front](https://github.com/3salles/eWallet-front).

* Documentação

Acesse a documentação deste projeto [ewallet/docs](https://ewallet-42d06a204d9c.herokuapp.com/openapi/swagger#).

Acesse esta API no Heroku [ewallet/transactions](https://ewallet-42d06a204d9c.herokuapp.com/transactions).



### :computer: Tecnologias

* [Flask](https://flask.palletsprojects.com/en/2.3.x)
* [Swagger](https://swagger.io/)
* [OpenAPI](https://www.openapis.org)
* [Sqlite](https://www.sqlite.org/index.html)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Docker](https://www.docker.com)

## :bricks: Instalação

Este projeto usa [Python](https://www.python.org) e [Virtualenv](https://virtualenv.pypa.io/en/latest/), você precisa deles para construir as dependências dele.

### :construction: Pré-requisitos

Clone o repositório deste projeto:

```bash

$ git clone https://github.com/3salles/eWallet-back.git

# Entre na pasta `eWallet-back`:

$ cd eWallet-back
```
🚨 Se você não possui o git na sua máquina, você pode instalá-lo [aqui](https://git-scm.com/downloads).

## file_cabinet Back-end

Este projeto pode ser rodado em um container do [Docker](https://www.docker.com).

Entre na pasta `eWallet-back` e rode os seguintes comandos:

```bash
$ docker build -t ewallet-back .

$ docker run -d -p 5001:5001 ewallet-back 
``` 

A aplicação estará disponível em `http://localhost:5001/transactions`.

### :construction: Instalando Dependências

Na pasta `eWallet`, crie um ambiente virtual com o virtualenv e ative-o:

```bash
$ virtualenv venv
$ source venv/bin/activate
```

Com o ambiente virtual ativado, instale os requerimentos deste projeto com os seguinte: comando:

```bash
$ pip install -r requirements.txt
```

### :arrow_forward: Rodando Back-end

Rode o seguinte comando para acessar a aplicação:

```bash
$ python3 app.py
```

A aplicação estará disponível em `http://localhost:5000/transactions`.


🚨 Se houver algum problema com o banco de dados, rode o arquivo `create_db.py` com o commando:

```bash
$ python3 create_db.py
```

E coloque o arquivo `database.db` criado na pasta `instance`:

```bash
$ mv database.py /tmp
```

E rode o projeto novamente.

## :page_facing_up: Licença

Este projeto usa licença [GPL](https://github.com/3salles/eWallet-back/blob/main/LICENSE).

## :woman_technologist: Autora

[Beatriz Salles](https://github.com/3salles)

<p align="center">Developed with 💜</p>
