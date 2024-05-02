from flask import Blueprint, render_template, jsonify, request, redirect, url_for

from board import database
from board.database import get_db

bp = Blueprint("workouts", __name__)

@bp.route('/workouts', methods=['POST'])
def add_workout():
    data = request.json
    exercise = data.get('exercise')
    reps = data.get('reps')
    sets = data.get('sets')

    if not exercise or not reps or not sets:
        return jsonify({'error': 'Incomplete data provided'}), 400

    database.insert_workout(exercise, reps, sets)

    # Redirect to the view page for the newly added workout
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT last_insert_rowid()')
    workout_id = cursor.fetchone()[0]
    return redirect(url_for('view_workout', id=workout_id))
    
    
# @bp.route('/viewworkout')
# def view_workout():
#     return render_template('workouts/view.html')

@bp.route('/workouts/<int:id>')
def view_workout(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM workouts WHERE id = ?', (id,))
    workout = cursor.fetchone()
    if workout:
        # Render data as HTML page
        return render_template('workout.html', workout=workout)
        # Or return data as JSON
        # return jsonify(workout)
    else:
        return 'Workout not found', 404