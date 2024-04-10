from flask import Flask
from config import Config

app=Flask(__name__)
app.config.from_object(Config)

from . import routes
from . import model

from . import form