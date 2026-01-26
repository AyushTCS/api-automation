import pytest
import requests
from pydantic import BaseModel, ValidationError
import time

BASE_URL = "https://jsonplaceholder.typicode.com"


class PostSchema(BaseModel):
    userId: int
    id: int
    title: str
    body: str


def test_response_time():
    start = time.time()
    response = requests.get(f"{BASE_URL}/posts")
    end = time.time()
    assert (end - start) < 2, "Response time exceeded 2 seconds"


def test_schema_validation():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    posts = response.json()
    for post in posts:
        try:
            PostSchema(**post)  # validate schema
        except ValidationError as e:
            pytest.fail(f"Schema validation failed: {e}")


@pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/users"])
def test_multiple_endpoints(endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}")
    assert response.status_code == 200, f"{endpoint} failed with {response.status_code}"
    assert response.json(), f"{endpoint} returned empty response"
