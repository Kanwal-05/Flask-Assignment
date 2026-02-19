# from flask import Flask, jsonify, request, render_template

# app = Flask(__name__)

# students = []


# # GET all students
# @app.route("/students")
# def get_students():
#     return jsonify(students)

# # GET student by ID
# @app.route("/students/<int:student_id>")
# def get_student(student_id):
#     for student in students:
#         if student["id"] == student_id:
#             return jsonify(student)
#     return jsonify({"error": "Student not found"}), 404

# # POST new student
# @app.route("/students", methods=["POST"])
# def add_student():
#     new_student = request.json

#     if not new_student or "id" not in new_student or "name" not in new_student or "class" not in new_student or "section" not in new_student:
#         return jsonify({"error": "Invalid input - Enter full details"}), 400

#     for student in students:
#         if student["id"] == new_student["id"]:
#             return jsonify({"error": "Student with this ID already exists"}), 400

#     students.append(new_student)
#     return jsonify({"message": "Student added", "student": new_student}), 201

# # DELETE student
# @app.route("/students/<int:student_id>", methods=["DELETE"])
# def delete_student(student_id):
#     for student in students:
#         if student["id"] == student_id:
#             students.remove(student)
#             return jsonify({"message": "Student deleted"}), 200
#     return jsonify({"error": "Student not found"}), 404

# # PATCH student
# @app.route("/students/<int:student_id>", methods=["PATCH"])
# def update_student(student_id):
#     data = request.json

#     for student in students:
#         if student["id"] == student_id:
#             if "name" in data:
#                 student["name"] = data["name"]
#             if "class" in data:
#                 student["class"] = data["class"]
#             if "section" in data:
#                 student["section"] = data["section"]

#             return jsonify({"message": "Student updated", "student": student}), 200

#     return jsonify({"error": "Student not found"}), 404

# # PUT student
# @app.route("/students/<int:student_id>", methods=["PUT"])
# def replace_student(student_id):
#     data = request.json

#     if not data or "id" not in data or "name" not in data or "class" not in data or "section" not in data:
#         return jsonify({"error": "PUT requires full student data"}), 400

#     if data["id"] != student_id:
#         return jsonify({"error": "ID mismatch"}), 400

#     for student in students:
#         if student["id"] == student_id:
#             student.update(data)
#             return jsonify({"message": "Student replaced", "student": student}), 200

#     return jsonify({"error": "Student not found"}), 404

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask , jsonify
app=Flask("Project 1")
data=[
    {
        "id": 1,
        "name":"Kanwal",
        "age": 23
    },
    {
        "id": 2,
        "name":"Sanskar",
        "age": 22
    },
    {
        "id": 3,
        "name":"Meenu",
        "age": 22
    },
    {
        "id": 4,
        "name":"Dilpreet",
        "age": 23
    },
    {
        "id": 5,
        "name":"Jaspreet",
        "age": 21
    }
]

@app.route("/")
def get_user():
    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)