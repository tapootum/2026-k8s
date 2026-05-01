from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics # เพิ่ม library
import psycopg2
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app) # สร้าง endpoint /metrics ให้อัตโนมัติ

# เพิ่มข้อมูล Static Info ให้ Prometheus
metrics.info('app_info', 'Backend Application info', version='1.0.0')

def get_db_connection():
    return psycopg2.connect(
        host='192.168.199.233',
        database='mydatabase',
        user='user',
        password='password',
        port=5432
        # host=os.getenv('localhost'),
        # database=os.getenv('mydatabase'),
        # user=os.getenv('user'),
        # password=os.getenv('password')
    )

@app.route('/add', methods=['POST'])
def add_message():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO messages (content) VALUES (%s)', (data['content'],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
