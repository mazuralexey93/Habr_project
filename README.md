# Комманды миграций бд
# При первой инициализации и создании таблиц в БД:

flask db init
flask db migrate -m "Initial migration."
flask db upgrade


# Пользовательские комманды создания и наполнения бд
flask init-db
flask create-init-user
flask create-init-post
