# ใช้ Node.js version 18 เป็น base image
FROM node:18-alpine

# สร้าง directory ทำงาน
WORKDIR /usr/src/app

# คัดลอก package.json เพื่อติดตั้ง dependencies ก่อน (ช่วยเรื่อง Layer Cache)
COPY package*.json ./

# ติดตั้ง express, axios สำหรับจัดการ request และ prom-client สำหรับ metrics
RUN npm install express axios prom-client

# คัดลอกโค้ดทั้งหมดเข้าเครื่อง
COPY . .

# เปิด port 3000 สำหรับหน้าเว็บและ /metrics
EXPOSE 3000

# รันแอปพลิเคชัน
CMD ["node", "server.js"]
