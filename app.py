from boggle import Boggle
from flask import redirect, Flask, request, render_template
from flask import session, make_response, flash, jsonify
boggle_game = Boggle()

app = Flask(__name__)

app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route("/")
def inits():
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("board.html", 
        board = session['board'], enum = enumerate)


@app.route("/guess")
def check_guess():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({"result" : response})