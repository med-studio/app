from dotenv import load_dotenv
import os
import sys

load_dotenv(dotenv_path="architecture/.env")
project_root = os.getenv("PROJECT_ROOT")

if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from architecture.infrastructure.src.components.calculator.knn import KNNClassifier
from architecture.infrastructure.src.components.calculator.zero_shot_classification import ZeroShotClassifier
from architecture.infrastructure.src.components.calculator.svm import SVMClassifier
from architecture.infrastructure.src.components.calculator.logistic_regression import LogisticRegression

class LogicalRouting:
    def __init__(self, classifier: KNNClassifier |
                                         SVMClassifier |
                                         LogisticRegression |
                                         ZeroShotClassifier = None) -> None:
        self.classifier = classifier
        if self.classifier is None:
            self.classifier = ZeroShotClassifier()
            
    def classify(self, query: str, documents: list) -> str:
        if isinstance(self.classifier, ZeroShotClassifier):
            return self.classifier.zero_shot(query, documents)
        else:
            return self.classifier.predict(query)