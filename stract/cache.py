from stract import cache
from stract import app
from stract import config

def clear():
    cache.init_app(app, config=config)
    with app.app_context():
        cache.clear()
