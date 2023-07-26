from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_title = db.Column(db.String)
    due_date = db.Column(db.Date)
    description = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False)
    users = db.relationship("Users", backref="project", lazy=True)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))