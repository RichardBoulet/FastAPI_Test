#!/usr/bin/env python

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression as LogReg
from typing import List

class Iris:
    
    def __init__(self):
        self.iris_type = {
            0: 'Setosa',
            1: 'Versicolor',
            2: 'Virginica'
        }
    
    def classify(self, features: List):
        
        # Load data
        iris = load_iris()
        X, y = iris.data, iris.target
        
        # Set parameters for logistic regression model
        clf = LogReg(solver = 'lbfgs', max_iter = 1_000, multi_class = 'multinomial')
        
        # Train model
        clf.fit(X,y)
                       
        # Predict given features in def             
        prediction = clf.predict_proba(features)
        
        return {'iris type prediction': self.iris_type[np.argmax(prediction)],
                'prediction probability': round(max(prediction[0]), 2)}

