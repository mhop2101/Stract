from flask import Flask
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.secret_key = "a very secure secret_key"
app.config.from_mapping(config)
cache = Cache(app)

from stract import routes
