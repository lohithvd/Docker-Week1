from flask import Flask, jsonify
import psycopg2
from flask_cors import CORS  # Move import to top

app = Flask(__name__)  # Instantiate only once
CORS(app)  # Ensure CORS is applied globally

# Function to get database connection
def get_db_connection():
    conn = psycopg2.connect(host='db', database='mydb', user='myuser', password='password')
    return conn

# Define the API route
@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM my_table;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Specify the port explicitly
