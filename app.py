from pydoc import render_doc
from random import random
from flask import Flask, render_template
import random

app = Flask(__name__)
randomWord = "apple"

@app.route("/")
def home():
    return render_template('index.html', word=randomWord)
