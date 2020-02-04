"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
from flask import request
from pusher import Pusher
import json

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

#For adding a todo list
@app.route('/add-todo', methods = ['POST'])
def addTodo():
    data = json.loads(request.data)
    pusher.trigger('todo', 'item-added', data)
    return jsonify(data)

    
#For deleting a task
@app.route('/remove-todo/<item_id>', methods = ['POST'])
def updateTodo(item_id):
    data = {'id': item_id }
    pusher.trigger('todo', 'item-removed', data)
    return jsonify(data)

# endpoint for updating todo item
@app.route('/update-todo/<item_id>', methods = ['POST'])
def updateTodo(item_id):
  data = {
    'id': item_id,
    'completed': json.loads(request.data).get('completed', 0)
  }
  pusher.trigger('todo', 'item-updated', data)
  return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


