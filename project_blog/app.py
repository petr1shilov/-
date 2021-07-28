from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///documents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Documents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Document %r>' % self.id
    


#Декоратор
@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


#Декоратор
@app.route('/create-doc', methods=['POST', 'GET'])
def create_doc():
    if request.method == "POST":
        rubrics = request.form['rubrics']
        text = request.form['text']

        doc = Documents(rubrics=rubrics, text=text)

        try:
            db.session.add(doc)
            db.session.commit()
            return redirect('/')
        except:
            return "ERROR"
        
    else:
        return render_template("create_document.html")


if __name__ == "__main__":
    app.run(debug=True)   