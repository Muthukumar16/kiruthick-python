from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "dev-secret"  # for flash messages

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Task {self.id} {self.title!r}>"

# Initialize DB (create if not exists)
with app.app_context():
    if not os.path.exists("tasks.db"):
        db.create_all()

@app.route("/")
def index():
    tasks = Task.query.order_by(Task.id.desc()).all()
    return render_template("index.html", tasks=tasks)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        if not title:
            flash("Title is required.", "error")
            return redirect(url_for("create"))
        task = Task(title=title, description=description or None)
        db.session.add(task)
        db.session.commit()
        flash("Task created successfully.", "success")
        return redirect(url_for("index"))
    return render_template("create.html")

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        if not title:
            flash("Title is required.", "error")
            return redirect(url_for("edit", task_id=task.id))
        task.title = title
        task.description = description or None
        db.session.commit()
        flash("Task updated successfully.", "success")
        return redirect(url_for("index"))
    return render_template("edit.html", task=task)

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully.", "success")
    return redirect(url_for("index"))

# Simple JSON APIs (optional)
@app.route("/api/tasks", methods=["GET"])
def api_list():
    tasks = Task.query.all()
    return [{"id": t.id, "title": t.title, "description": t.description} for t in tasks]

@app.route("/api/tasks", methods=["POST"])
def api_create():
    data = request.get_json(force=True)
    title = (data.get("title") or "").strip()
    description = (data.get("description") or "").strip()
    if not title:
        return {"error": "Title is required"}, 400
    task = Task(title=title, description=description or None)
    db.session.add(task)
    db.session.commit()
    return {"id": task.id, "title": task.title, "description": task.description}, 201

@app.route("/api/tasks/<int:task_id>", methods=["PUT", "PATCH"])
def api_update(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json(force=True)
    if "title" in data:
        new_title = (data["title"] or "").strip()
        if not new_title:
            return {"error": "Title cannot be empty"}, 400
        task.title = new_title
    if "description" in data:
        task.description = (data["description"] or "").strip() or None
    db.session.commit()
    return {"id": task.id, "title": task.title, "description": task.description}

@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def api_delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return {"status": "deleted", "id": task.id}
