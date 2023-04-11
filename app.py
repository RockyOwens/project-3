from flask import Flask, jsonify
import psycopg2
import json
from flask_cors import CORS

conn = psycopg2.connect (
    dbname = ‘ ……… ’,
    user = ‘postgres’,
    password = ‘postgres’,
    host = ‘localhost’,
    port =‘5432’
)
app = Flask(__name__)
CORS(app)
@ app.route(‘/data’)
def data():
    cur = conn.cursor()
    cur.execute(‘SELECT * FROM ……. ;’)
    data = cur.fetchall()
    cur.close()
    headers = [desc[0] for desc in cur.description]
    result = [dict(zip(headers, row)) for row in data]
    print(‘Data accessed from database:’, data)
    return jsonify(result)
if __name__ == ‘__main__‘:
    app.run(debug=True)







