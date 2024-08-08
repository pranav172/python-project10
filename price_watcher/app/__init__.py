from flask import Flask
from config import Config
from flask_apscheduler import APScheduler

scheduler = APScheduler()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app import routes
    
    scheduler.init_app(app)
    scheduler.start()

    return app