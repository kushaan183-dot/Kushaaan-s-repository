from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("calculate",methods=["POST"])
def calculate():
    units= int(request.form["units"])
    bill=units*5
    if units <= 100:
        message="Great, your an energy saver!🌱"
    elif units <= 200:
        message="Good, try saving a litle more! 👍"
    elif units <200:
        message="Whoa! Time to turn of so lightes! 💡"
    return render_template("index.html",units=units,bill=bill,message=message)
if __name__=="__main__":
    app.run(debug=True)