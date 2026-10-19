from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)