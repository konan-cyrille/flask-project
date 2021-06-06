## Create virtual environnment
`python3 -m venv my_env`

## install dependancies:
`pip install -r requirements.txt`

## Initialize database

`flask db init`

## save migration
`flask db migrate -m "users table"`
`
## Create Users table
`flask db upgrade`

## run flask server:
`python run_app.py`
