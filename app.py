from flask import Flask
from flask_ask import Ask, statement, question, session

import requests

app = Flask(__name__)
ask = Ask(app, '/telljokes')

def getJoke():
    return "random joke"
    pass

@app.route('/')
def homepage():
    return 'Welcome to Alexa Jokes Library'

@ask.launch
def start_skill():
    message = 'Hey.. would you like to hear a Joke'
    return question(message)

@ask.intent("YesIntent")
def share_joke():
    joke = getJoke()
    message_Joke = 'Here is a joke for you!{}'.format(joke)
    return statement(message_Joke)

@ask.intent("NoIntent")
def no_Intent():
    message = 'Well that is fine... Maybe your humor will wake up some day!'
    return statement(message)

@ask.intent("CancelIntent")
def cancel_Intent():
    message = 'See you again...bye'
    return statement(message)

if __name__ == '__main__':
    app.run(threaded = True)