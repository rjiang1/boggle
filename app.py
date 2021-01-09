from boggle import Boggle
from flask import redirect, Flask, request, render_template
from flask import session, make_response, flash
boggle_game = Boggle()

app = Flask(__name__)

app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

board = Boggle()
layout = board.make_board()

@app.route("/")
def inits():
    session['layout'] = layout
    return redirect("/board")

@app.route("/board")
def show_board():
    
    return render_template("board.html", 
        board = layout, enum = enumerate)

# @app.route("/guess")
# def check_guess():
#     word = request.form['word_guess']
#     if word.lower() in board.words:
#         print('hello')
#     else:
#         flash("That is not a word in the word list")

#     return redirect("/board")