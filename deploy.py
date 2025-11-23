from flask import Flask, render_template,  request
import pickle

app = Flask(__name__)
#load the model
model=pickle.load(open('finalized_model.sav','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict', methods=['POST','GET'])
def predict():
    age =float(request.form['age'])
    sex = float(request.form['sex']) 
    symptom_age = float(request.form['symptom_age'])
    diagnosis_age =float(request.form['diagnosis_age'])
    bdi1_total= float(request.form['bdi1_total'])
    audit1_total =float(request.form['audit1_total'])
    aas1_total= float(request.form['aas1_total'] )
    psy1004_grade= float(request.form['psy1004_grade'])
    nbt_ave = float(request.form['nbt_ave'])
    matric_mark= float(request.form['matric_mark'])
    asrs1_total.x = float(request.form['asrs1_total.x'])
    bai1_total= float(request.form['bai1_total'])
    result = model.predict([[age,sex,symptom_age,diagnosis_age,bdi1_total,audit1_total,aas1_total,psy1004_grade,nbt_ave,matric_mark,asrs1_total.x,bai1_total]])
    return render_template('index.html',**locals())

if __name__ =='__main__':
    app.run(debug=True)


#zsh: command not found: python3
#python3 -m pip install flask pandas numpy matplotlib seaborn scikit-learn statsmodels wordcloud

