from fastapi import FastAPI
from app.schemas import QARequest, QAResponse
from app.model import QAModel

app = FastAPI(title="Question Answering API")
model = QAModel()

@app.post("/predict", response_model=QAResponse)
async def predict(request: QARequest):
    """
    Predict the answer to a question based on the provided context.

    Parameters:
    - request: QARequest object containing the question and context.

    Returns:
    - QAResponse object containing the predicted answer.
    """
    answer = model.predict(request.question, request.context)
    return {
        "answer": answer["answer"],
        "score": answer["score"]
    }

@app.get("/")
async def root():
    return {"Message": "Hello, change the url to /docs to see the API documentation."}