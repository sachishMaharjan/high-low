from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


@app.route("/")
def home():
    return '<h1> Guess a number between 0 and 9 <h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"> </img>'


@app.route("/<int:input_number>")
def check_number(input_number):
    if input_number < random_number:
        return '<h1 style="color:red"> Too Low, try again <h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"> </img>'
    elif input_number > random_number:
        return '<h1 style="color:purple"> Too High, try again <h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"> </img>'
    else:
        return '<h1 style="color:green"> You Found me! <h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"> </img>'


if __name__ == "__main__":
    app.run(debug=True)