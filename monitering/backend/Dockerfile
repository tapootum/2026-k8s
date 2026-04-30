# ใช้ Python 3.9 แบบ slim เพื่อให้ image มีขนาดเล็ก
FROM python:3.9-slim

# ตั้งค่าไม่ให้ Python สร้างไฟล์ .pyc และให้แสดง log ทันที
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ติดตั้งระบบพื้นฐานที่จำเป็นสำหรับ psycopg2 (ตัวเชื่อมต่อ Postgres)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# ติดตั้ง Library ที่จำเป็น
# flask: สำหรับทำ API
# psycopg2-binary: สำหรับต่อ Database
# prometheus-flask-exporter: สำหรับพ่น metrics ไป Prometheus
RUN pip install --no-cache-dir flask psycopg2-binary prometheus-flask-exporter

# คัดลอกโค้ดแอปพลิเคชัน
COPY . .

# เปิด port 5000 สำหรับ API และ /metrics
EXPOSE 5000

# รันแอปพลิเคชัน
CMD ["python", "app.py"]
