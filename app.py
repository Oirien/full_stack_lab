from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# for new project changes tasks_app to DB name
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://rob:123@localhost:5432/project_user_lab"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.projects_controller import projects_blueprint

from models import Users, Project

app.register_blueprint(projects_blueprint)