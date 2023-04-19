from flask import Flask, render_template, request
import numpy as np
import cv2
from Models import model

model = model.get()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        dist = request.form.get('dist')
        season = request.form.get('season')
        area = request.form.get('area')
        imagefile = request.files['imagefile']
        img = cv2.imdecode(np.fromstring(imagefile.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (300, 300))
        img = img.reshape((1,) + img.shape)
        yhat = model.predict(img)
        classification = yhat[0]
        return render_template('index.html', prediction=classification)
    else:
        return render_template('index.html')



if __name__=='__main__':
    app.run(port=3000, debug=True)
