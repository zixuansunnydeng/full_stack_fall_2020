
from flask import Flask
from flask import request
app = Flask(__name__)
html = """
<form action="/another_route" method="POST">
    <h1>hello</h1>
    <input type="number">
<form>
</html>
"""
@app.route('/')
def hello_world():
  return html
@app.route('/another_route')
def another_route():
  q = request.args.get('q')
  return q