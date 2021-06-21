from flask import Flask,render_template,request
import numpy as np
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def predt():
    try:
        fea=float(request.form['salary'])
        pred=[[fea]]
        predicition=model.predict(pred)[0][0]
        return render_template('index.html',res='salary is {:.2f}'.format(predicition))
    except:
        return render_template('index.html',error='Error Occured. Enter Valid Number')




    
if __name__=='__main__':
    app.run()
