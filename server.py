from flask import Flask, render_template, request
from Models import make_preds

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            dist = request.form.get('district')
            season = request.form.get('season')
            area = request.form.get('area')
            imagefile = request.files['imagefile']
            
            preds = make_preds.get_yield(imagefile=imagefile, dist=dist, season=season, area=area)
            app.logger.info(f'Prediction succeeded for imagefile {imagefile.filename}')

            return render_template('index.html', prediction=preds)
        except Exception as e:
            app.logger.error(f'Prediction failed: {e}')
            return render_template('error.html', error_message=str(e))
    else:
        return render_template('index.html')


if __name__=='__main__':
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])
