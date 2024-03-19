from flask import Flask, jsonify, g
import pandas as pd
import sqlite3

app = Flask(__name__)
DATABASE = 'movies.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def load_data():
    conn = get_db()
    df = pd.read_csv('movielist.csv', delimiter=';')
    chunksize = int(len(df) / 10)
    df.to_sql('movies', conn, if_exists='append', index=False, chunksize=chunksize)


def calculate_intervals():
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('''SELECT producer, MIN(year) AS previousWin, MAX(year) AS followingWin, 
                      MAX(year) - MIN(year) AS interval 
                      FROM (SELECT producers AS producer, year FROM movies WHERE winner = 'yes') 
                      GROUP BY producer HAVING COUNT(*) > 1
                      ORDER BY interval ASC''')

    min_interval = cursor.fetchall()

    cursor.execute('''SELECT producer, MIN(year) AS previousWin, MAX(year) AS followingWin, 
                      MAX(year) - MIN(year) AS interval 
                      FROM (SELECT producers AS producer, year FROM movies WHERE winner = 'yes') 
                      GROUP BY producer HAVING COUNT(*) > 1
                      ORDER BY interval DESC''')

    max_interval = cursor.fetchall()

    return min_interval, max_interval

@app.route('/load-data', methods=['GET'])
def load_data_route():
    load_data()
    return jsonify({"message": "Data loaded successfully"}), 200

@app.route('/producers', methods=['GET'])
def get_producers():
    min_interval, max_interval = calculate_intervals()
    min_producers = [dict(ix) for ix in min_interval]
    max_producers = [dict(ix) for ix in max_interval]

    response = {
        "min": min_producers,
        "max": max_producers
    }

    return jsonify(response), 200

if __name__ == '__main__':
    with app.app_context():
        init_db()
        load_data()
    app.run(debug=True)
