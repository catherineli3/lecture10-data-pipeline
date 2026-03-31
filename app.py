from flask import Flask, render_template, jsonify
import sqlite3
from pathlib import Path
import json


app = Flask(__name__)
DB_PATH = Path(__file__).parent / 'data' / 'orders.db'


def get_db_connection():
    """Create a database connection."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def get_orders():
    """Retrieve all orders from the database."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders')
        orders = cursor.fetchall()
        return [dict(row) for row in orders]
    finally:
        conn.close()


def get_summary():
    """Retrieve region summary from the database."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM region_summary ORDER BY avg_amount_cny DESC')
        summary = cursor.fetchall()
        return [dict(row) for row in summary]
    finally:
        conn.close()


@app.route('/')
def index():
    """Main page showing orders and summary."""
    orders = get_orders()
    summary = get_summary()
    return render_template('index.html', orders=orders, summary=summary)


@app.route('/api/orders')
def api_orders():
    """API endpoint for orders data (for auto-refresh)."""
    return jsonify(get_orders())


@app.route('/api/summary')
def api_summary():
    """API endpoint for summary data (for auto-refresh)."""
    return jsonify(get_summary())


if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(parents=True, exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
