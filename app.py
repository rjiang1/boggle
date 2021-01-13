from boggle import Boggle
from flask import redirect, Flask, request, render_template
from flask import session, make_response, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()

app = Flask(__name__)

app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

nplays = 0
hi_score = 0

@app.route("/")
def inits():
    """Home page where it loads and hosts the game board"""
    board = boggle_game.make_board()
    session["board"] = board
    html_board = session["board"]

    highscore = session.get("hi_score", 0)
    nplays = session.get("nplays", 0)

    return render_template("board.html", board=html_board,
                           highscore=highscore,
                           nplays=nplays, enum=enumerate)


@app.route("/guess")
def check_guess():
    """This route verifys if the submitted word from the 
        front end is valid by using a method from the boggle
        file in boggle.py. Returns a HTTP response with 3 
        possible reponses."""

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({"result" : response})

@app.route("/finished", methods=["POST"])
def finished_game():
    """This route takes the score at the end of the game
    and compares it with the high score stroed on the backend.
    It return a json object with the current high score, either 
    the new one that just beat the old one or the old one if the
    new score did not beat the old one."""
    
    score = request.json["score"]
    hi_score = session.get("hi_score", 0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays+1
    session['hi_score'] = max(score,hi_score)
    hi_score = session['hi_score']

    return jsonify({"new_hi" : hi_score})