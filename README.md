# MVC-Fastapi API
FastApi CRUD MYSQL with concept MVC

#### 1. Saya menggunakan Anaconda
#### 2. Buat lingkugan kerja (environment) Anaconda

Di direktori repo utama
```shell
    conda env create -f envs/environment.yml
    conda activate fastapi
    pip freeze > envs/requirements.txt

```

## Menginstal dengan semua dependensi pada FastApi
```shell
pip install "fastapi[all]"
```

## Menginstall dependensi secara terpisah
Lihat Referensi klik di <a href=https://afrizalmy.com/tutorial-fastapi-crud-dengan-mysql> sini </a> 
dan <a href="https://fastapi.tiangolo.com/"> ini </a>
```
pip install fastapi
pip install "uvicorn[standard]"
pip install SQLAlchemy
pip install alembic
pip install PyMysql
pip install Faker