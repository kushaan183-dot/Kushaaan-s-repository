from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        name="",
        goal=0,
        glasses=0,
        remaining=0,
        message="",
        status="",
    )


@app.route("/track", methods=["POST"])
def track():
    name = request.form.get("name", "")
    goal = int(request.form.get("goal", 0))
    glasses = int(request.form.get("glasses", 0))

    remaining = max(goal - glasses, 0)
    if glasses >= goal:
        status = "success"
        message = f"🎉 Success! {name} reached the goal!"
    else:
        status = "warning"
        message = f"💧 Keep going! {name} still needs {remaining} more glasses."

    return render_template(
        "index.html",
        name=name,
        goal=goal,
        glasses=glasses,
        remaining=remaining,
        message=message,
        status=status,
    )


if __name__ == "__main__":
    app.run(debug=True)
