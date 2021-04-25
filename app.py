#imports 
from flask import Flask, render_template, redirect
import sqlite3
import pandas as pd 

# create instance of Flask app
app = Flask(__name__)

# create connection to build new db if nonexistent and cursor to execute queries
conn = sqlite3.connect('static/data/nba_test')
c = conn.cursor()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    with sqlite3.connect('static/data/nba_test') as conn:
        c = conn.cursor() 

# Find one record of data from the mongo database
        kobe_data = pd.read_sql('''SELECT * FROM kobe LIMIT 10''', conn)
        points = (kobe_data["pts"])
    return points 
    conn.close()
    
if __name__ == "__main__":
    app.run(debug=True)


