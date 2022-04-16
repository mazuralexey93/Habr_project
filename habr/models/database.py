from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import enum
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()


class CategoryChoices(enum.Enum):
    DESIGN = 'design'
    WEB = 'web'
    MOBILE = 'mobile'
    MARKETING = 'marketing'

    def __str__(self):
        return self.value
