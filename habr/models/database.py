from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()
migrate = Migrate()


class CategoryChoices(enum.Enum):
    DESIGN = 'design'
    WEB = 'web'
    MOBILE = 'mobile'
    MARKETING = 'marketing'

    def __str__(self):
        return self.value
