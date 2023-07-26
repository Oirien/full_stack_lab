from flask import Flask, render_template, Blueprint, redirect, request
from app import db
from models import Users, Project


projects_blueprint = Blueprint("project", __name__)

@projects_blueprint.route("/")
def project():
    return render_template("index.jinja")

@projects_blueprint.route("/projects")
def projects():
    projects = Project.query.all()
    return render_template("projects/index.jinja", projects=projects)

@projects_blueprint.route("/projects/new")
def new_project():
    return render_template("projects/new.jinja")

@projects_blueprint.route("/projects", methods=['POST'])
def add_project():
    project_title = request.form["project_title"]
    description = request.form["description"]
    due_date = request.form["due_date"]
    completed = "completed" in request.form

    project = Project(project_title = project_title, description = description, due_date = due_date, completed = completed)

    db.session.add(project)
    db.session.commit()

    return redirect("/projects")

@projects_blueprint.route("/projects/<id>")
def show_project(id):
    project = Project.query.get(id)
    users = Users.query.all()
    return render_template("projects/show.jinja", project=project, users=users)

@projects_blueprint.route("/projects/<id>/add_user", methods=["POST"])
def afba(id):
    result = request.form["blue"]
    result = int(result)
    user = Users.query.get(result)

    user.project_id = id

    db.session.commit()
    return redirect("/projects")