from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()
    current_year = now.year
    current_day = now.day
    current_now = now
    current_month = now.strftime("%B")
    return render_template("index.html", now=current_now, year=current_year, month=current_month, day=current_day)


@app.route('/card')
def card():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    randomRank = random.choice(ranks)
    randomSuit = random.choice(suits)
    return render_template("card.html", rank=randomRank, suit=randomSuit)

@app.route('/about')
def about():
    pageData = "Welcome to the About page!" 
    return render_template("about.html", pageData=pageData)

@app.route('/contact')
def contact():
    pageData = "Welcome to the Contact page!"
    return render_template("contact.html", pageData=pageData)
