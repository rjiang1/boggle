from boggle import Boggle
from flask import redirect, Flask, request, render_template, session, make_response
boggle_game = Boggle()

app = Flask(__name__)

@app.route("/board")
def show_board():
    board = Boggle()
    layout = board.make_board()
    return render_template("board.html", board = layout, enum = enumerate)