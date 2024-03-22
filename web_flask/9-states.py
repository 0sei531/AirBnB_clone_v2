#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def display_states(id=None):
    """Displays an HTML page with a list of all States or info about a specific state."""
    states = storage.all("State").values()
    state = None
    if id:
        state = storage.get("State", id)
    return render_template("9-states.html", states=states, state=state)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
