# เช็คชื่อ 
### Week 4 https://forms.gle/3Apfu8EHiadf1JMv7
### Week 5 https://forms.gle/Vtb4Gng8Xf413F9b9
### Week 9 https://forms.gle/CH9Nvh8uDLMVY1Hj7

#Install ingress
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml
```

# Home work Week 4
1. Deploy Jenkins and Grafana on kubernetes.
2. Create github repo with https://github.com/user-name/b5124817-xxxxx
   - Create folder jenkins and grafana
   - Add file
     - deployment.yaml
     - service.yaml
     - pv.yaml
     - pvc.yaml
     - ingress.yaml
     - Screen capture web browser
   - if deploy fail -> capture log on kubernetes and write detail of error.
3. Don't forget map domain in file hosts.

![Jenkins](jenkins.png)
![Grafana](grafana.png)
