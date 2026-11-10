import sqlite3
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# Laboratory Activity 7: connect to the SQLite database made by init_db.py
def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00271",
        "name": "Rochelle Ann Paclibar",
        "program": "BSIT",
        "year": 3,
        "section": "Dijkstra"
    })


@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')
    return jsonify({
        "message": f"Hello, {name}!"
    })


# Custom API endpoint for Laboratory Activity 6
@app.route('/course')
def get_course():
    return jsonify({
        "course_code": "IT 3120",
        "course_name": "System Integration",
        "program": "BSIT",
        "year": 3
    })


# Laboratory Activity 7: all students from the database
@app.route('/students')
def get_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()

    return jsonify([dict(student) for student in students])


# Laboratory Activity 7: one student by database ID
@app.route('/students/<int:id>')
def get_student_by_id(id):
    conn = get_db_connection()
    student = conn.execute(
        'SELECT * FROM students WHERE id = ?', (id,)
    ).fetchone()
    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(dict(student))


# Laboratory Activity 7 additional task: students in one section (read from the database)
@app.route('/students/section/<section>')
def get_students_by_section(section):
    conn = get_db_connection()
    students = conn.execute(
        'SELECT * FROM students WHERE LOWER(section) = LOWER(?)', (section,)
    ).fetchall()
    conn.close()

    return jsonify([dict(student) for student in students])


if __name__ == '__main__':
    app.run(debug=True)