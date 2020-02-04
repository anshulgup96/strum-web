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
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email not in users:
            return render_template("index.html", message="Incorrect email or password")
        if users[email] == password:
            return render_template("index.html", message ="Successfully Logged In")
        return render_template("index.html", message="Incorrect email or password")
    return render_template("index.html")

"""
@app.route('/api/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}
"""
@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")

@app.route("/page")
def page():
    return render_template('page.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


