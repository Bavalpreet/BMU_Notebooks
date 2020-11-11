import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd



app = Flask(__name__)

# LOADING OUR SAVED MODELS
model = pickle.load(open('/home/bavalpreet/Documents/flask_modelhost/model.pkl', 'rb'))


# UNPICKLING OUR 3 LABEL ENCODERS
le_s=pickle.load(open("/home/bavalpreet/Documents/flask_modelhost/label-encoders/le_sex.pickle","rb"))

le_smoker=pickle.load(open("/home/bavalpreet/Documents/flask_modelhost/label-encoders/le_smoker.pickle","rb"))

le_region=pickle.load(open("/home/bavalpreet/Documents/flask_modelhost/label-encoders/le_region.pickle","rb"))

# print(dict(zip(le_s.classes_, le_s.transform(le_s.classes_))))
# print(dict(zip(le_smoker.classes_, le_smoker.transform(le_smoker.classes_))))
# print(dict(zip(le_region.classes_, le_region.transform(le_region.classes_))))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    data={}
    data['age']=[str(request.form.get('age'))]
   
    data['sex']=[str(request.form.get('sex'))]

    data['bmi']=[str(request.form.get('bmi'))]


    data['children']=[str(request.form.get('children'))]

    data['smoker']=[str(request.form.get('smoker'))]


    data['region']=[str(request.form.get('regions'))]

    data=pd.DataFrame.from_dict(data)

    print('Before transforming the data \n', data)

    # label encoding our 3 categorical columns using our Label encoder objects
    data['sex']=le_s.transform(data['sex'])
    data['smoker']=le_smoker.transform(data['smoker'])
    data['region']=le_region.transform(data['region'])


    print('After transforming data \n', data)
    
    # converting dataframe to numpy for prediction
    final_features = data.to_numpy()

    prediction = model.predict(final_features)
    
    output = round(prediction[0][0],2)

    return render_template('index.html', prediction_text='Insurance prize should be nearly $ {}'.format(output))
    


if __name__ == "__main__":
    app.run(debug=True)