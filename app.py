from pydoc import render_doc
from random import random
#from urllib import request
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
randomWord = 'apple'
censoredRandomWord = []

for i in range(len(randomWord)):
    censoredRandomWord.append('_')

guesses = []

@app.route("/")
def home():
    return render_template('index.html', word=censoredRandomWord, guesses=guesses)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    guess=request.form['wordToGuess']
    if(guess == randomWord):
        for i in range(len(randomWord)):
            censoredRandomWord[i]=randomWord[i]
        print('you won')
        return 'you won'

    result = ''
    for i in range(len(randomWord)):
        if(guess == randomWord[i]):
            result = randomWord[i]
            censoredRandomWord[i]=result
        
    if(result == ''):
        guesses.append(guess)

    rightLetterCount = 0
    for i in range(len(randomWord)):
        if censoredRandomWord[i] == randomWord[i]:
            rightLetterCount += 1
        print(rightLetterCount)
        if rightLetterCount == len(randomWord):
            print('you won')
            return 'you won'

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()