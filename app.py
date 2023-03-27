from flask import Flask, render_template
from database import load_communities_from_db


app = Flask(__name__)




@app.route("/")
def hello_communities():
  communities = load_communities_from_db()
  return render_template('home.html', communities=communities)

@app.route("/api/communities")
def list_communities():
  return jsonify(COMMUNITIES)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)