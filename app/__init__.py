from flask import Flask

from setting import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)

# Installer l'extension flask-wtf pour utiliser CSRF
# app.config["SECRET_KEY"] = "eviter les attaques CSRF(seasurf)"

# une manière plus intéligettent de definir la configuration
app.config.from_object(Config)

# instanciate SQLALchemy object
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# la ligne ci dessous permet d'import dans le package toute les fuctions du fichier views.py
from app import views, models