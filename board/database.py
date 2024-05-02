import sqlite3
from flask import g, current_app
import os

def init_app(app):
    app.config['DATABASE'] = 'workouts.db'
    with app.app_context():
        db = get_db()
        with current_app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode('utf8'))
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db

def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def insert_workout(exercise, reps, sets):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO workouts (exercise, reps, sets) VALUES (?, ?, ?)', (exercise, reps, sets))
    db.commit()