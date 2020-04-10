from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# SECRET_KEY is needed for session security, the flash() method in this case stores the messages in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kkcpoesdonqzia:46d1387c593e32025d8320e84008f823b30b8c2d711c8d77549a7e18529b2f6b@ec2-54-197-250-121.compute-1.amazonaws.com:5432/d5rgvvn3dq1e1t'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True  # added just to suppress a warning
from app import views


