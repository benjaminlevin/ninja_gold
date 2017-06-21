from flask import Flask, render_template, request, redirect, session
import random
import time
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/', methods=['GET'])
def index():
    try:
        if session['activity'] == None:
            session['activity'] = []
        if session['wallet'] == None:
            session['wallet'] = int(0)
        if session['status'] == None:
            session['status'] = {}
    except KeyError:
        session['activity'] = []
        session['wallet'] = int(0)
        session['status'] = {}
    session['time'] = time.strftime('%Y/%m/%d %I:%M %p')
    return render_template('index.html')

@app.route('/process_money')
def process_money():
    session['wallet'] = session['gold'] + session['wallet']
    return redirect('/')

@app.route('/reset')
def reset():
    session['wallet'] = int(0)
    session['activity'] = []
    session['status'] = []
    return redirect('/')

@app.route('/farm', methods=['POST'])
def farm():
    session['gold'] = random.randrange(10,21)
    session['activity'].append('Earned ' + str(session['gold']) + ' golds from the farm! ' + str(session['time']))
    return redirect('/process_money')

@app.route('/cave', methods=['POST'])
def cave():
    session['gold'] = random.randrange(5,11)
    session['activity'].append('Earned ' + str(session['gold']) + ' golds from the cave! ' + str(session['time']))
    return redirect('/process_money')

@app.route('/house', methods=['POST'])
def house():
    session['gold'] = random.randrange(2,6)
    session['activity'].append('Earned ' + str(session['gold']) + ' golds from the house! ' + str(session['time']))
    return redirect('/process_money')

@app.route('/casino', methods=['POST'])
def casino():
    session['gold'] = random.randrange(-50,51)
    if session['gold'] < int(0):
        session['activity'].append(('Lost ' + str(session['gold'] * -1) + ' golds from the casino... ouch! ' + str(session['time'])))
    elif session['gold'] >= int(0):
        session['activity'].append('Earned ' + str(session['gold']) + ' golds from the casino! ' + str(session['time']))
    return redirect('/process_money')

app.run(debug=True)
