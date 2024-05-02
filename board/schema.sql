DROP TABLE IF EXISTS workouts;

CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exercise VARCHAR(100),
    reps INTEGER,
    sets INTEGER
);