"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

users = {
    "anshul@email.com": "anshul",
    "tilak@email.com": "password",
    "kunal@gmail.com": '12345'
}

@app.route("/", methods=["GET", "POST"])
def homepage():
    """View function for Home Page."""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if users[email] == password:
            return render_template("index.html", message ="Successfully Logged In")
        return render_template("index.html", message="Incorrect email or password")
    return render_template("index.html")



@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
