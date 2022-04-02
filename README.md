# Комманды миграций бд
# При первой инициализации и создании таблиц в БД:

python -m flask db init
python -m flask db migrate -m "Initial migration."
python -m flask db upgrade




# Пользовательские комманды создания и наполнения бд
python -m flask init-db
python -m flask create-init-user
python -m flask create-init-post
