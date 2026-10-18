
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to my first API!"


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


# New Endpoint 1: Course Information
@app.route('/course')
def get_course():
    name = request.args.get('name', 'IT3120')
    return jsonify({
        "course": name,
        "description": "Deploying a Flask API Online"
    })


# New Endpoint 2: Personalized Greeting
@app.route('/greet/<name>')
def greet_person(name):
    return jsonify({
        "message": f"Welcome, {name}!"
    })


if __name__ == '__main__':
    app.run(debug=True)
