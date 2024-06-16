import requests
r = requests.post("http://158.160.116.205:8000/predict", json={"data":"скидка два процента"})
print(r.content)