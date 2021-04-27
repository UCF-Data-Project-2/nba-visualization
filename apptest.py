#imports 
import pandas as pd
from sqlalchemy import create_engine
import json
import numpy as np
from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import csv 

# Create an instance of Flask
app = Flask(__name__)

#kobe csv 
df = pd.read_csv(open('kobe_data.csv'))
columns = df.columns.values

#lebron csv 
df = pd.read_csv(open('lebron_data.csv'))
columns = df.columns.values

#connects to my database
engine = create_engine( )
conn = engine.connect()

#connects to my database
engine = create_engine( )
conn = engine.connect()

#print("'{}'," * 53)
with open('static/db/players.json', 'r') as pt:
    players_json = json.load(pt)

#for i in columns:
#    print("row['{}'], ".format(i))

@app.route("/")
def home():
    return render_template("index.html")

####kobe db test 


def table_initialization():
    conn.execute('''CREATE TABLE "kobe Stats" ("Index" varchar(50) NOT NULL, PRIMARY KEY ("Index"));''')
    for column in columns:
        print(column)
        if column != 'Index':
            conn.execute('''ALTER TABLE "kobe Stats" ADD COLUMN "{}" VARCHAR(50);'''.format(str(column)))

def data_insertion():
    counter = 0
    for index, row in df.iterrows():
        if int(row['Index']) > 195:
            if "'" in str(row['Player']):
                player = str(row['Player']).replace("'", '')
                conn.execute('''INSERT INTO "kobe Stats" VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(row['Index'], row['Year'], player, row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS']))
            else:
                conn.execute('''INSERT INTO "kobe Stats" VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(row['Index'], row['Year'], row['Player'], row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS']))
            counter += 1
            if counter % 200 == 0:
                print(row['Index'], row['Year'], row['Player'], row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS'])
data_insertion()

###Lebron codb test

def table_initialization():
    conn.execute('''CREATE TABLE "lebron Stats" ("Index" varchar(50) NOT NULL, PRIMARY KEY ("Index"));''')
    for column in columns:
        print(column)
        if column != 'Index':
            conn.execute('''ALTER TABLE "lebron Stats" ADD COLUMN "{}" VARCHAR(50);'''.format(str(column)))

def data_insertion():
    counter = 0
    for index, row in df.iterrows():
        if int(row['Index']) > 195:
            if "'" in str(row['Player']):
                player = str(row['Player']).replace("'", '')
                conn.execute('''INSERT INTO "lebron Stats" VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(row['Index'], row['Year'], player, row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS']))
            else:
                conn.execute('''INSERT INTO "lebron Stats" VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(row['Index'], row['Year'], row['Player'], row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS']))
            counter += 1
            if counter % 200 == 0:
                print(row['Index'], row['Year'], row['Player'], row['Pos'], row['Age'], row['Tm'], row['G'], row['GS'], row['MP'], row['PER'], row['TSPercent'], row['3PAr'], row['FTr'], row['ORBPercent'], row['DRBPercent'], row['TRBPercent'], row['ASTPercent'], row['STLPercent'], row['BLKPercent'], row['TOVPercent'], row['USGPercent'], row['blanl'], row['OWS'], row['DWS'], row['WS'], row['WS/48'], row['blank2'], row['OBPM'], row['DBPM'], row['BPM'], row['VORP'], row['FG'], row['FGA'], row['FGPercent'], row['3P'], row['3PA'], row['3PPercent'], row['2P'], row['2PA'], row['2PPercent'], row['eFGPercent'], row['FT'], row['FTA'], row['FTPercent'], row['ORB'], row['DRB'], row['TRB'], row['AST'], row['STL'], row['BLK'], row['TOV'], row['PF'], row['PTS'])
data_insertion()

@app.route("/")
def home():
    return render_template("index.html")

