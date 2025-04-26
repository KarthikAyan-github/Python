# Importing Flask framework to develop web app
from flask import Flask, render_template

# Creating flask object
app = Flask(__name__)

#if user in  root display home page
@app.route('/')
def home():
  return render_template("home.html")

#if user in  /students display students page
@app.route('/students')
def student_list():
    return render_template('students.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)