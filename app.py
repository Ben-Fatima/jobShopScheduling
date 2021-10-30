import base64
from random import shuffle
from flask import Flask, render_template, request, send_from_directory

def merge(L, P):
  if len(L) == 0:
    return P
  if len(P) == 0:
    return L
  if L[0] in P:
    i = P.index(L[0])
    return P[0:i + 1] + merge(L[1:], P[i+1:])
  else:
    return [L[0]] + merge(L[1:], P)

def greedy(jobs):
  solution = jobs[0]
  for i in range(1, len(jobs)):
    solution = merge(solution, jobs[i])
  return solution

def decode(data):
  data = base64.b64decode(data.encode('ascii')).decode('ascii')
  data = data.split('\n')
  return [x.split(' ') for x in data]

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/static/<path>')
def oppo(path):
  print(path)
  return send_from_directory('templates/static', path)

@app.route('/solve')
def solve():
  jobs = decode(request.args.get('data'))
  best = greedy(jobs)
  for i in range(0, 1000):
    shuffle(jobs)
    solution = greedy(jobs)
    if (len(solution) < len(best)):
      best = solution
  return ' '.join(best)


  
