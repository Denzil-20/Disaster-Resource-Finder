from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///resources.db"
db = SQLAlchemy(app)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

@app.route("/")
def home():
    return render_template("resources.html")

@app.route("/api/resources")
def get_resources():
    query = request.args.get("type")
    resources = Resource.query.all()

    if query:
        resources = [r for r in resources if r.type.lower() == query.lower()]

    return jsonify([
        {"id": r.id, "name": r.name, "type": r.type,
         "latitude": r.latitude, "longitude": r.longitude}
        for r in resources
    ])

if __name__ == "__main__":
    app.run(debug=True)
