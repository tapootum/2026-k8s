# Ubuntu
```bash
sudo apt insatll nginx
sudo systemctl start nginx
```
---
# Nginx
```bash
sudo nginx -t #ตรวจสอบความถูกต้องของ syntax
sudo nginx -s reload # reload nginx config
```

---
# Run APP
```bash
cd app1
uvicorn main:app --host 0.0.0.0 --port 8000
cd app2
uvicorn main:app --host 0.0.0.0 --port 8080
cd app3
uvicorn main:app --host 0.0.0.0 --port 8001
cd app4
uvicorn main:app --host 0.0.0.0 --port 8081
```

---
# CURL
```bash
curl -X {GET,POST,PUT,DELETE} -H "X-API-KEY: abc1234" http://localhost/v1/
curl -X GET -H "X-API-KEY: abc1234" http://localhost/v1/

curl -X {GET,POST,PUT,DELETE} -H "X-API-KEY: xyz5678" http://localhost/v2/
curl -X POST -H "X-API-KEY: xyz5678" http://localhost/v2/
```
