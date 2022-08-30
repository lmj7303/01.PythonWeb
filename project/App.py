from unittest import result
from flask import Flask, render_template, request
import os
import tensorflow as tf
import numpy as np
from tensorflow import keras

model = keras.models.load_model('only_train.h5')

app=Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/upload',methods=['POST'])
def upload():
    f_image= request.files['file']
    fname = f_image.filename
    #filename = os.path.join(app.static_folder, 'upload/') + fname
    #f_image.save(filename)
    f_image.save('C:/Workspace/project/static/upload/'+fname+'.jpg')
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True)