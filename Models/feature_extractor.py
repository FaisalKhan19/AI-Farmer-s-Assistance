from sklearn.base import BaseEstimator, TransformerMixin

class FeatureExtractorTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, feature_extractor_model):
        self.feature_extractor_model = feature_extractor_model
        
    def fit(self, X, y=None):
        return self
        
    def transform(self, X, y=None):
        # Reshape the input from (num_samples, height, width, channels) to (num_samples, height, width, channels)
        X = X.reshape(X.shape[0], X.shape[1], X.shape[2], -1)
        
        # Use the feature_extractor_model to obtain the feature vectors for each input image
        return self.feature_extractor_model.predict(X)