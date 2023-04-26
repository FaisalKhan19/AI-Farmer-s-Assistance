import numpy as np
import cv2
from Models import model, make_input

model, model_rfs = model.get()

def get_yeild(imagefile, dist, season, area):
        img = cv2.imdecode(np.fromstring(imagefile.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (300, 300))
        img = img.reshape((1,) + img.shape)
        label = model.predict(img)
        label = label[0]
        df = make_input.make_data(district=dist,season=season,label=label,area=area)
        preds = model_rfs.predict(df)
        yeilds = make_input.map_yeilds(pred=preds, label=label)
        return yeilds