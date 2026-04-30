const express = require('express');
const axios = require('axios');
const client = require('prom-client'); // เพิ่ม library

const app = express();
app.use(express.urlencoded({ extended: true }));

// สร้าง Registry สำหรับเก็บ Metrics
const register = new client.Registry();
client.collectDefaultMetrics({ register });

// สร้าง Custom Metric: นับจำนวนคนกดโพสต์
const postCounter = new client.Counter({
  name: 'frontend_posts_total',
  help: 'Total number of posts submitted via frontend',
});
register.registerMetric(postCounter);

app.get('/', (req, res) => {
    res.send(`<form method="POST" action="/post"><input type="text" name="message"><button type="submit">Send</button></form>`);
});

app.post('/post', async (req, res) => {
    try {
        const backendUrl = process.env.BACKEND_URL || 'http://192.168.199.233:5000';
        await axios.post(`${backendUrl}/add`, { content: req.body.message });
        postCounter.inc(); // เพิ่มค่า Metric เมื่อมีคนโพสต์สำเร็จ
        res.send('Success!');
    } catch (err) {
        res.status(500).send('Error');
    }
});

// Endpoint สำหรับ Prometheus มา Scrape
app.get('/metrics', async (req, res) => {
    res.setHeader('Content-Type', register.contentType);
    res.end(await register.metrics());
});

app.listen(3000, () => console.log('Frontend metrics on :3000/metrics'));
