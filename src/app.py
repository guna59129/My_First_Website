from flask import Flask, json, render_template,jsonify

app = Flask(__name__)

jobs=[
  {
    'id':'1',
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':'2',
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':'3',
    'title':'Backend Engineer',
    'location':'San Fransciso, USA',
    'salary':'$120,000'
  },
  {
    'id':'4',
    'title':'Frontend Engineer', 
    'location':'Remote',
    'salary':'Rs. 15,00,000'
  }
]
@app.route('/')
def hello():
  return render_template("home.html",jobs=jobs,companyname='Guna')

@app.route('/api/jobs')
def listjobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
