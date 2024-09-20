from flask import Flask
from flaskr.models import db

#updating it to use forms 16-09-24

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'
app.config['SECRET_KEY'] = 'd8b99972f00fd6c57e72e70f16bb07d6'
db.init_app(app)

from flaskr import routes