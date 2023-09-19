<p align="center">

  <h3 align="center">eWallet</h3>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Lincense&message=GPL&color=0000ff" alt="License" />
</p>

<p align="center">
    This API was created to be used by eWallet (a financial website) developed for a postgraduate course in Software Engineering at PUC-Rio
    <br />
    <a href="README.md">🇺🇸English</a>
    ·
    <a href="README-pt.md">🇧🇷Portuguese</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## 🗂 Table of Contents

* [About the Project](#book-about-the-project)
  * [Technologies](#computer-technologies)
* [Installation](#bricks-installation)
  * [Prerequisites](#construction-prerequisites)
  * [Back-end](#file_cabinet-back-end)
    * [Installing Dependencies](#construction-installing-dependencies)
    <!-- * [Setting Back-end](#wrench-setting-back-end) -->
    * [Running Back-end](#arrow_forward-running-back-end)
* [License](#page_facing_up-license)
* [Authors](#woman_technologist-author)

## :book: About The Project

This is an API to eWallet a financial website developed to obtain grade at PUC-Rio.

Link to access front-end project: [eWallet-front](https://github.com/3salles/eWallet-front).

* Documentation

Access this API documentation [ewallet/docs](https://ewallet-back.onrender.com/openapi/swagger#).

Access this API on onRender [ewallet/transactions](https://ewallet-back.onrender.com/transactions).



### :computer: Technologies

* [Flask](https://flask.palletsprojects.com/en/2.3.x)
* [Swagger](https://swagger.io/)
* [OpenAPI](https://www.openapis.org)
* [Sqlite](https://www.sqlite.org/index.html)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Docker](https://www.docker.com)

## :bricks: Installation

This project uses [Python](https://www.python.org) and [Virtualenv](https://virtualenv.pypa.io/en/latest/), you will need it to build its dependencies.

### :construction: Prerequisites

Clone this project repository:

```bash

$ git clone https://github.com/3salles/eWallet-back.git

# Enter in `eWallet-back` folder:

$ cd eWallet-back
```

🚨 If you don't have git in your machine, you can install it [here](https://git-scm.com/downloads).

## :file_cabinet: Back-end

This project can be used with [Docker](https://www.docker.com) container.

In `eWallet-back` folder, run following commands:
```bash
$ docker build -t ewallet-back .

$ docker run -d -p 5001:5001 ewallet-back 
``` 
The application will be available on `http://localhost:5001/transactions`.

### :construction: Installing Dependencies

In `eWallet-back` folder, create a virtual environment with virtualenv and activate it:

```bash
$ virtualenv venv
$ source venv/bin/activate
```

With virtual environment activated, install this project's requirements with the following command:

```bash
$ pip install -r requirements.txt
```

### :arrow_forward: Running Back-end

Run the following command to access the application:

```bash
$ python3 app.py
```

The application will be available on `http://localhost:5000/transactions`.


🚨 If there is any problem with database, run the file `create_db.py` with the command:

```bash
$ python3 create_db.py
```

And put the created `database.db` file into folder `instance`:

```bash
$ mv database.py /tmp
```

Then run the project again

## :page_facing_up: License

This project uses [GPL](https://github.com/3salles/eWallet-back/blob/main/LICENSE) license.

## :woman_technologist: Author

[Beatriz Salles](https://github.com/3salles)

<p align="center">Developed with 💜</p>
