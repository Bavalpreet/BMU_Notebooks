import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':19, 'bmi':200, 'children':400, 'sex_female':1, 'sex_male':0,'smoker_no':0,'smoker_yes':1,'region_northeast':0,'region_northwest':0,'region_southeast':0,'region_southwest':1
})

print(r.json())

