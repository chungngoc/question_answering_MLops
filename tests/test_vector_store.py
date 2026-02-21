from app.vector_store import VectorStore

def test_vector_store_search(mocker):
    '''Test the search functionality of the VectorStore class.'''
    mock_embedder = mocker.Mock()
    mock_embedder.encode.return_value = [[0.1, 0.2, 0.3]]

    # Mock the EmbeddingModel to return the mock embedder
    mocker.patch(
        "app.embeddings.EmbeddingModel",
        return_value=mock_embedder
    )

    # Mock the load_document function to return a predefined set of documents
    mocker.patch(
        "app.vector_store.load_document",
        return_value=[
            {"text": "doc1", "source": "a"},
            {"text": "doc2", "source": "b"},
        ]
    )

    vector_store = VectorStore()
    results = vector_store.search("test", top_k=1)

    assert len(results) > 0
    assert "text" in results[0]
    assert "source" in results[0]