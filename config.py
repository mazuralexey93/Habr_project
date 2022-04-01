import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '@thereisnospoon4!'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'habr.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # сигнализировать приложению каждый раз,
                                            # когда в базе данных должно быть внесено изменение.
