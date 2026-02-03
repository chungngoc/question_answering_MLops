from transformers import pipeline

class QAModel:
    def __init__(self):
        self.pipeline = pipeline(
            "question-answering",
            model="distilbert-base-cased-distilled-squad"
        )

    def predict(self, question:str, context:str)-> dict:
        result = self.pipeline(
            question=question,
            context=context
        )
        return result