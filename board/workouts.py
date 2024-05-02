from flask import Blueprint, render_template, jsonify, request, redirect, url_for

from board import database
from board.database import get_db

bp = Blueprint("workouts", __name__)

@bp.route('/workouts', methods=['GET', 'POST'])
def add_workout():
    if request.method == 'POST':
        data = request.form
        exercise = data.get('exercise')
        reps = data.get('reps')
        sets = data.get('sets')

        if not exercise or not reps or not sets:
            return jsonify({'error': 'Incomplete data provided'}), 400

        # Add the workout to the database (you can add this part later)

        # Redirect to a different page after successful submission
        return redirect(url_for('workouts.view_workout'))
    else:
        # If GET request, render the add.html template
        return render_template('workouts/add.html')
    
    
# @bp.route('/viewworkout')
# def view_workout():
#     return render_template('workouts/view.html')

@bp.route('/viewworkout')
def view_workout():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM workouts ORDER BY id DESC LIMIT 1')
    workout = cursor.fetchone()

    if workout is None:
        return jsonify({'error': 'No workouts found'}), 404

    return jsonify({
        'id': workout['id'],
        'exercise': workout['exercise'],
        'reps': workout['reps'],
        'sets': workout['sets']
    })
