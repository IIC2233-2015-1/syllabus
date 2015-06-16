import os
from flask import Flask, request, jsonify, render_template, Response
from student import Student

# Initialization
app = Flask(__name__)
app.debug = True

students = {s.id: s for s in [
    Student("Patricio Lopez", "MrPatiwi", True),
    Student("Jaime Castro", "jecastro1", False),
    Student("Belen Saldias", "bcsaldias", False)
]}


def param_to_bool(data):
    return data is not None and data.lower() == 'true'


# Controllers
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/students", methods=['GET', 'POST'])
def students_index():
    if request.method == 'GET':
        items = [s.serialize() for (identifier, s) in students.items()]
        return jsonify(students=items)

    elif request.method == 'POST':
        name = request.args.get('name')
        username = request.args.get('username')
        assistance = param_to_bool(request.args.get('assistance'))

        if name and username and assistance:
            unique = not any(v.username.lower() == username.lower()
                         for k, v in students.items())
            if unique:
                student = Student(name, username, assistance)
                students[student.id] = student
                return jsonify(student.serialize()), 201

        return Response(status=400)

    else:
        return Response(status=405)


@app.route("/students/<student_id>", methods=['GET', 'DELETE', 'PATCH'])
def student(student_id):
    if student_id.isdigit() == False:
        return Response(status=404)

    student_id = int(student_id)

    if student_id not in students:
        return Response(status=404)

    if request.method == 'GET':
        return jsonify(students[student_id].serialize())

    elif request.method == 'DELETE':
        return jsonify(students.pop(student_id, None).serialize())

    elif request.method == 'PATCH':
        student = students[student_id]
        student.assistance = param_to_bool(request.args.get('assistance'))
        return jsonify(student.serialize()), 202

    else:
        return Response(status=405)


# Start app
if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get("PORT", 5001))
    )
