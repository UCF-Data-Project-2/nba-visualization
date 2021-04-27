from flask import Flask, render_template, redirect
import requests
import json
import sqlite3 as sql
from sqlite3 import Error
import pandas as pd
from datetime import datetime

# Create an instance of Flask
app = Flask(__name__)




# Route to render index.html template using data from Sqlite
@app.route("/")
def getResults():
    results = getPoints()

    xAxis = results[1]
    yAxis = results[0]

    return render_template("index.html", xAxis=xAxis, yAxis=yAxis)

def getPoints():

    """ create a database connection to a SQLite database """
    conn = None
    try:
        with sql.connect("nba_test") as conn:
            c = conn.cursor()
            # query total points per year for Kobe
            kb_points = c.execute('''SELECT ROW_NUMBER() OVER (
                ORDER BY strftime('%Y', [game.date])
                )row_num,
                strftime('%Y', [game.date]) as Year, SUM(pts) 
                FROM kobe 
                WHERE pts IS NOT NULL 
                GROUP BY Year''').fetchall()
            lj_points = c.execute('''SELECT ROW_NUMBER() OVER (
                ORDER BY strftime('%Y', [game.date])
                )row_num,
                strftime('%Y', [game.date]) as Year, SUM(pts) 
                FROM kobe 
                WHERE pts IS NOT NULL 
                GROUP BY Year''').fetchall()    
            
            # Declare vars
            pList = []
            yList = []

            #iterate through ist and ush values into a list
            for i in kb_points:
                pList.append(int(i[1]))
                yList.append(int(i[0]))
            
            yAxis = [pList]
            xAxis = [yList]
            results = []    
            results.extend((yAxis, xAxis))
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    # Return template and data
    return (results)



if __name__ == "__main__":
    app.run(debug=True)