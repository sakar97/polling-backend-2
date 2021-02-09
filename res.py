from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

poll_data = {
   'question' : 'Choose One',
   'fields'   : ['Option1','Option2']
}

datafile = "data.txt"

@app.route('/res')
def res():
    r = requests.get(os.environ['CONTAINER_IP'])
    return render_template('a.html', data=r.text)

@app.route('/results')
def show_results():
    votes = {}
    for f in poll_data['fields']:
        votes[f] = 0

    f  = open(datafile, 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1

    return render_template('results.html', data=poll_data, votes=votes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
