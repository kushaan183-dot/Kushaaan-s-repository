from flask import Flask, render_template, request

app = Flask(__name__)


def get_bmi_category(bmi):
    if bmi is None:
        return None
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obesity"


@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    error = None

    if request.method == "POST":
        weight_text = request.form.get("weight", "").strip()
        height_text = request.form.get("height", "").strip()

        try:
            weight = float(weight_text)
            height = float(height_text)
        except ValueError:
            error = "Please enter valid numeric values."
        else:
            if weight <= 0 or height <= 0:
                error = "Weight and height must be greater than zero."
            else:
                bmi = round(weight / (height ** 2), 2)
                category = get_bmi_category(bmi)

    return render_template("index.html", bmi=bmi, category=category, error=error)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
