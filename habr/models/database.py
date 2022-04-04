from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()
migrate = Migrate()


class CategoryChoices(enum.Enum):
    DESIGN = 'design'
    WEB = 'deb'
    MOBILE = 'mobile'
    MARKETING = 'marketing'

    @staticmethod
    def fetch_categories():
        return [c.value for c in CategoryChoices]
