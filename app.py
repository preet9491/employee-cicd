
from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

employees = []

courses = [
    "AWS Cloud Fundamentals",
    "Docker & Containers",
    "CI/CD with GitHub Actions",
    "Python Programming"
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Employee Training Portal</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            margin: 0;
            padding: 30px 15px;
        }

        .container {
            max-width: 550px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 15px #0001;
        }

        h1 {
            text-align: center;
            color: #2457a7;
        }

        input, select, button {
            width: 100%;
            box-sizing: border-box;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            background: #2457a7;
            color: white;
            border: none;
            cursor: pointer;
        }

        .employee {
            background: #edf7ed;
            padding: 12px;
            margin-top: 10px;
            border-radius: 6px;
        }
    </style>
</head>

<body>
<div class="container">

    <h1>Employee Training Portal</h1>

    <p>Register for your preferred employee training program.</p>

    <form action="/register" method="POST">

        <input
            type="text"
            name="name"
            placeholder="Employee Name"
            required
        >

        <input
            type="email"
            name="email"
            placeholder="Email Address"
            required
        >

        <select name="course" required>
            <option value="">Select Training Course</option>

            {% for course in courses %}
                <option value="{{ course }}">{{ course }}</option>
            {% endfor %}

        </select>

        <button type="submit">Register Now</button>

    </form>

    <h2>Registered Employees</h2>

    {% for employee in employees %}

        <div class="employee">
            <strong>{{ employee.name }}</strong><br>
            {{ employee.email }}<br>
            Training: {{ employee.course }}
        </div>

    {% else %}

        <p>No employees registered yet.</p>

    {% endfor %}

</div>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def home():
    return render_template_string(
        HTML,
        employees=employees,
        courses=courses
    )


@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not email or course not in courses:
        return "Invalid registration details", 400

    employees.append({
        "name": name,
        "email": email,
        "course": course
    })

    return redirect(url_for("home"))


@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
