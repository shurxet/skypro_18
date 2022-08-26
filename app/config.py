# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

# Пример

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
    #SECRET_HERE = '249y823r9v8238r9u'
