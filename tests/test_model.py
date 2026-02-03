from app.model import QAModel

def test_qa_model_returns_answer():
    model = QAModel()

    question = "What is MLOps?"
    context = (
        "MLOps is a set of practices that combines machine learning and DevOps to deploy and maintain models in production."
    )

    result = model.predict(question, context)

    assert "answer" in result
    assert isinstance(result["answer"], str)
    assert len(result["answer"]) > 0