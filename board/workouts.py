from flask import Blueprint, render_template, jsonify, request, redirect, url_for

from board import database
from board.database import get_db

bp = Blueprint("workouts", __name__)

@bp.route('/workouts', methods=['GET', 'POST'])
def add_workout():
    if request.method == "POST":
        # Extract data from the form
        exercise = request.form.get('exercise')
        reps = request.form.get('reps')
        sets = request.form.get('sets')

        if not exercise or not reps or not sets:
            return jsonify({'error': 'Incomplete data provided'}), 400

        database.insert_workout(exercise, reps, sets)

        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT last_insert_rowid()')
        workout_id = cursor.fetchone()[0]

        
        cursor.execute('SELECT * FROM workouts WHERE id = ?', (workout_id,))
        workout = cursor.fetchone()

        if workout:
            # Convert the workout object to a dictionary
            workout_dict = dict(workout)

            return jsonify(workout_dict)
        else:
            return 'Workout not found', 404
    return render_template("workouts/add.html") 

@bp.route('/view', methods=['GET', 'POST'])
def view_workout():
    if request.method == "POST":
        workout_id = request.form.get('workout_id')

        if workout_id:
            return redirect(url_for('workouts.show_workout', id=workout_id))  # Replace '1' with the actual ID of the newly inserted workout
        else:
            return 'No workout ID provided', 400
    else:
        return render_template("workouts/view.html")
    
@bp.route('/view/<int:id>')
def show_workout(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM workouts WHERE id = ?', (id,))
    workout = cursor.fetchone()

    if workout:
        # Convert the workout object to a dictionary
        workout_dict = dict(workout)

        return render_template('workouts/show.html', workout=workout_dict)
        #return jsonify(workout_dict)
    else:
        return 'Workout not found', 404
    

# @bp.route('/workouts', methods=['GET', 'POST'])
# def add_workout():
#     if request.method == "POST":
#         # Extract data from the form
#         exercise = request.form.get('exercise')
#         reps = request.form.get('reps')
#         sets = request.form.get('sets')

#         if not exercise or not reps or not sets:
#             return jsonify({'error': 'Incomplete data provided'}), 400

#         database.insert_workout(exercise, reps, sets)

#         # Redirect to the view page for the newly added workout
#         db = get_db()
#         cursor = db.cursor()
#         cursor.execute('SELECT last_insert_rowid()')
#         workout_id = cursor.fetchone()[0]
#         return redirect(url_for('workouts.view_workout', id=workout_id))  # Replace '1' with the actual ID of the newly inserted workout
#     return render_template("workouts/add.html") 

# @bp.route('/workouts/<int:id>')
# def view_workout(id):
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute('SELECT * FROM workouts WHERE id = ?', (id,))
#     workout = cursor.fetchone()

#     if workout:
#         # Convert the workout object to a dictionary
#         workout_dict = dict(workout)
        
#         # Add the id to the workout dictionary
#         workout_dict['wotkout_id'] = id

#         return jsonify(workout_dict)
#     else:
#         return 'Workout not found', 404