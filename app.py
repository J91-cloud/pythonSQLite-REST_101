import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # import both flash_sqlalchemy and SQLAlchemy

class Config:
    SECRET_KEY = 'your_secret_key'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'main.db')  # Database URI, in this case main will what our database will be called.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy()


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from controller.controllers import main_bp

app.register_blueprint(main_bp)


@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
