from flask import Flask, redirect
from flask import request
from flask.helpers import url_for
from flask.templating import render_template
app = Flask(__name__)
html = """
<form action="/foo" method="POST">
    <input type="text" name="q">
  <input type="submit" value="submit this">
<form>
</html>
"""
@app.route('/')
def hello_world():
  return html

@app.route('/foo', methods=['GET', 'POST'])
def foo():
  if request.method == 'POST':
    q = request.form['q']
    # do stuff with q, save it somewhere
    return redirect(url_for('bar', q=q))
  else:
    return 'This is foo'

@app.route('/bar')
def bar():
  q = request.args['q']
  return render_template('thanks.html', q=q)
