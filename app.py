from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        ism = request.form.get('ism')
        email = request.form.get('email')
        xabar = request.form.get('xabar')

        return render_template("info.html", ism=ism, email=email, xabar=xabar)
    
    return render_template('index.html')




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
