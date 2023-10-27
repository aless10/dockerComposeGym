from app.main import ping


def test_ping():
    result = ping()
    assert result == {"message": "Hello, FastAPI in Docker!"}
