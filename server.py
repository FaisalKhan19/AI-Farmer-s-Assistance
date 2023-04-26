from flask import Flask, render_template, request
from Models import make_preds
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        dist = request.form.get('district')
        season = request.form.get('season')
        area = request.form.get('area')
        imagefile = request.files['imagefile']
        
        preds = make_preds.get_yeild(imagefile=imagefile, dist=dist, season=season, area=area)

        return render_template('index.html', prediction=preds)
    else:
        return render_template('index.html')



if __name__=='__main__':
    app.run(port=3000, debug=True)
