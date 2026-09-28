from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/result")
def result():
    name = "Rahul"
    percentage = 65
    return render_template(
"result.html",
name=name,
percentage=percentage
)
app.run(debug=True,port=5001)