import tensorflow as tf
import numpy as np
import pickle
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler 
from Models.feature_extractor import FeatureExtractorTransformer
import cv2
import os

os.chdir("C://Users//Faisal Ali Khan//Downloads//train_data")
X = []
Y = []
i=1
for dirc in os.listdir():
    path = "C://Users//Faisal Ali Khan//Downloads//train_data\\{}".format(dirc)
    for f in os.listdir(path):
        path = "C://Users//Faisal Ali Khan//Downloads//train_data\\{}\\{}".format(dirc,f)
        img = cv2.resize(cv2.imread(path),(300,300))
        X.append(img)
        Y.append(i)
    i+=1
X = np.array(X)
Y = np.array(Y)


script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
with open("grid_search_model.pkl", 'rb') as file:
    model_rfs = pickle.load(file)
model_n1 = tf.keras.models.load_model("Model_N1")
model_output = model_n1.layers[10].output
model_input = model_n1.inputs
model_FE = tf.keras.models.Model(inputs=model_input, outputs=model_output)

svm_clf = SVC()
model = pipeline = Pipeline([
    ('feature_extractor', FeatureExtractorTransformer(model_FE)),
    ('scaler', StandardScaler()),
    ('svm', svm_clf)
])
model.fit(X,Y)

def get():
    return model,model_rfs
