from contextlib import contextmanager
import sqlite3
from sqlite3 import Error
from flask import Flask, render_template, redirect, jsonify, request,  send_from_directory


#------------------------------------------------------------#
# Create variable for database file
#------------------------------------------------------------#

DB_FILE = "static/data/nba_test.db"


#------------------------------------------------------------#
# Establish connection to database
#------------------------------------------------------------#

@contextmanager
def connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        yield sqlite3.connect(DB_FILE)
    except Error as e: 
        print(e)
    finally:
        if conn:
            conn.close()


#------------------------------------------------------------#
# Send data to browser via connection
#------------------------------------------------------------#

# Gives us all data in database file
def read_all_data():
    with connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM players")

        data = []
        for row in cur.fetchall():
            data.append(
                {
                    "name": row[0],
                    "team_id": row[1],
                    "player_id": row[2],
                    "season": row[3]
                }
            )

        return data

# Gives us data with parameters for season year
def get_all_data_by_year(year: int):
    with connection() as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM players WHERE SEASON = {year} ")

        data = []
        for row in cur.fetchall():
            data.append(
                {
                    "name": row[0],
                    "team_id": row[1],
                    "player_id": row[2],
                    "season": row[3]
                }
            )

        return data

#------------------------------------------------------------#
# Create an instance of Flask
#------------------------------------------------------------#

app = Flask(__name__)


#------------------------------------------------------------#
# Route to render index.html
#------------------------------------------------------------#

@app.route("/")
def home():
    return render_template('index.html')

#------------------------------------------------------------#
#Establish routes
#------------------------------------------------------------#

@app.route("/api")
def api():
    year = request.args.get('year')
    if year:
        try:
            year = int(year)
            print(year)

            return jsonify(get_all_data_by_year(year))
        except ValueError:
            pass


@app.route("/api/all")
def all_data():
    return jsonify(read_all_data())


if __name__ == "__main__":
    app.run(debug=True)
