from flask import Flask, render_template

app = Flask(__name__)

COMMUNITIES =[
 {
    'id': 1,
    'No. of Members': '40',
    'title': 'Virtual Code Club',
    'location': 'Bhopal'
 },
  {
     'id': 2,
    'No. of Members': '50',
    'title': 'Anime Club',
    'location': 'Delhi'
  },
 {
    'id': 3,
    'No. of Members': '50',
    'title': 'Music Club',
    'location': 'Mumbai'
  }
]

@app.route("/")
def hello_communities():
  return render_template('home.html', communities=COMMUNITIES)

@app.route("/api/communities")
def list_communities():
  return jsonify(COMMUNITIES)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)