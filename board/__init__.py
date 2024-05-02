import os
from dotenv import load_dotenv
from flask import Flask, jsonify

from board import pages, workouts, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    database.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(workouts.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app