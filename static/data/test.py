from contextlib import contextmanager
import sqlite3
from sqlite3 import Error
import pandas as pd

DB_FILE = r"nba_test.db"


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


def populate_data():
    with connection() as conn:
        c = conn.cursor()
        print(sqlite3.version)
        c.execute(
            '''CREATE TABLE players (PLAYER_NAME text, TEAM_ID text, PLAYER_ID text, SEASON int)''')
        players = pd.read_csv('players.csv')
        players.to_sql('players', conn, if_exists='append', index=False)


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


if __name__ == '__main__':
    create_connection(r"nba_test.db")
    print(len(read_all_data()))
    print(len(get_all_data_by_year(2019)))
