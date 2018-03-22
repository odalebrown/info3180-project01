from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password12@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True  # added just to suppress a warning
from app import views


