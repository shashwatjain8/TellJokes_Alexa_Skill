from flask import Flask
from flask_ask import Ask, statement, question, session
import random
import requests
import pandas as pd

app = Flask(__name__)
ask = Ask(app, '/telljokes')

df = pd.read_csv('funjokes.csv')


def getJoke():
    x = random.randint(1,9984)
    return df.iloc[x]['Joke']

@app.route('/')
def homepage():
    return 'Welcome to Alexa Jokes Library'

@ask.launch
def start_skill():
    message = 'Hey.. would you like to hear a Joke?'
    return question(message)

@ask.intent("YesIntent")
def share_joke():
    joke = getJoke()
    message_Joke = 'Here is a joke for you!{}'.format(joke)
    return statement(message_Joke)

@ask.intent("NoIntent")
def no_Intent():
    message = 'Well that is fine... Maybe your sense of humor will wake up some day! Haha just kidding!'
    return statement(message)

@ask.intent("AMAZON.CancelIntent")
def cancel_Intent():
    message = 'See you again...bye'
    return statement(message)

@ask.intent("AMAZON.StopIntent")
def stop_Intent():
    message = 'See you again...bye'
    return statement(message)

@ask.intent("AMAZON.HelpIntent")
def help_Intent():
    message = 'Say yes to hear a joke'
    return question(message)

if __name__ == '__main__':
    app.run(threaded = True)