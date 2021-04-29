from contextlib import contextmanager
import sqlite3  as sql
from sqlite3 import Error
from flask import Flask, render_template, redirect, jsonify, request,  send_from_directory


#------------------------------------------------------------#
# Create variable for database file
#------------------------------------------------------------#

DB_FILE = "static/data/nba_test"


#------------------------------------------------------------#
# Establish connection to database
#------------------------------------------------------------#

@contextmanager
def connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        yield sql.connect(DB_FILE)
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
        c = conn.cursor()
        
        # Kobe stats all data
        kb_all_data = c.execute('''
            SELECT 
            ROW_NUMBER() OVER (ORDER BY strftime('%Y', [game.date]))
            row_num,strftime('%Y',[game.date]) as Year,strftime('%Y-%m-%d',[game.date]) as Date,[game.visitor_team_id],[game.home_team_id],pts,ast,reb,blk,dreb,stl  
            FROM kobe 
            WHERE pts IS NOT NULL
            ''').fetchall()
        # Kobe stats per year data
        kb_yearly_data = c.execute('''
            SELECT 
            ROW_NUMBER() OVER (ORDER BY strftime('%Y', [game.date]))
            row_num,strftime('%Y', [game.date]) as Year,sum(pts),sum(ast),sum(reb),sum(blk),sum(dreb),sum(stl) 
            FROM kobe 
            WHERE pts IS NOT NULL
            GROUP BY Year
            ''').fetchall()

        # Lebron stats all data
        lj_all_data = c.execute('''
            SELECT 
            ROW_NUMBER() OVER (ORDER BY strftime('%Y', [game.date]))
            row_num,strftime('%Y',[game.date]) as Year,strftime('%Y-%m-%d',[game.date]) as Date,[game.visitor_team_id],[game.home_team_id],pts,ast,reb,blk,dreb,stl  
            FROM lebron 
            WHERE pts IS NOT NULL
            ''').fetchall()   
        # Lebron stats per year data
        lj_yearly_data = c.execute('''
            SELECT 
            ROW_NUMBER() OVER (ORDER BY strftime('%Y', [game.date]))
            row_num,strftime('%Y', [game.date]) as Year,sum(pts),sum(ast),sum(reb),sum(blk),sum(dreb),sum(stl) 
            FROM lebron 
            WHERE pts IS NOT NULL
            GROUP BY Year
            ''').fetchall()
             

        # yearly stats arrays
        kb_year_index = [] #0
        kb_pts_yr = [] #2
        kb_ast_yr = [] #3
        kb_reb_yr = [] #4
        kb_blk_yr = [] #5
        kb_dreb_yr = [] #6
        kb_stl_yr = [] #7
        # individual games stats arrays
        kb_year = [] #1
        kb_date = [] #2
        kb_pts = [] #5
        kb_ast = [] #6
        kb_reb = [] #7
        kb_blk = [] #8
        kb_dreb = [] #9
        kb_stl = [] #10

        for i in kb_yearly_data:
            kb_year_index.append(int(i[0])) #0
            kb_pts_yr.append(int(i[2])) #2
            kb_ast_yr.append(int(i[3])) #3
            kb_reb_yr.append(int(i[4])) #4
            kb_blk_yr.append(int(i[5])) #5
            kb_dreb_yr.append(int(i[6])) #6
            kb_stl_yr.append(int(i[7])) #7

        for i in kb_all_data:
            kb_year.append(int(i[1])) #1
            kb_date.append(i[2]) #2
            kb_pts.append(int(i[5])) #5
            kb_ast.append(int(i[6])) #6
            kb_reb.append(int(i[7])) #7
            kb_blk.append(int(i[8])) #8
            kb_dreb.append(int(i[9])) #9
            kb_stl.append(int(i[10])) #10
        

        # yearly stats arrays
        lj_year_index = [] #0
        lj_pts_yr = [] #2
        lj_ast_yr = [] #3
        lj_reb_yr = [] #4
        lj_blk_yr = [] #5
        lj_dreb_yr = [] #6
        lj_stl_yr = [] #7
        # individual games stats arrays
        lj_year = [] #1
        lj_date = [] #2
        lj_pts = [] #5
        lj_ast = [] #6
        lj_reb = [] #7
        lj_blk = [] #8
        lj_dreb = [] #9
        lj_stl = [] #10

        for i in lj_yearly_data:
            lj_year_index.append(int(i[0])) #0
            lj_pts_yr.append(int(i[2])) #2
            lj_ast_yr.append(int(i[3])) #2
            lj_reb_yr.append(int(i[4])) #4
            lj_blk_yr.append(int(i[5])) #5
            lj_dreb_yr.append(int(i[6])) #6
            lj_stl_yr.append(int(i[7])) #7

        for i in lj_all_data:
            lj_year.append(int(i[1])) #1
            lj_date.append(i[2]) #2
            lj_pts.append(int(i[5])) #5
            lj_ast.append(int(i[6])) #6
            lj_reb.append(int(i[7])) #7
            lj_blk.append(int(i[8])) #8
            lj_dreb.append(int(i[9])) #9
            lj_stl.append(int(i[10])) #10
        # Kim's original code
        # data = []
        # for row in c.fetchall():
        #     data.append(
        #         {
        #             "name": row[0],
        #             "team_id": row[1],
        #             "player_id": row[2],
        #             "season": row[3]
        #         }
        #     )

        return data

# Gives us data with parameters for season year
def get_all_data_by_year(year: int):
    with connection() as conn:
        c = conn.cursor()
        c.execute(f"SELECT * FROM players WHERE SEASON = {year} ")

        data = []
        for row in c.fetchall():
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
