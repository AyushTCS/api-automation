import pytest
import requests
from pydantic import BaseModel, ValidationError
import time
import json
import os


class PostSchema(BaseModel):
    userId: int
    id: int
    title: str
    body: str


@pytest.mark.api
def test_response_time(api_base_url):
    start = time.time()
    response = requests.get(f"{api_base_url}/posts")
    end = time.time()
    assert (end - start) < 2


@pytest.mark.api
def test_schema_validation(api_base_url):
    response = requests.get(f"{api_base_url}/posts")
    assert response.status_code == 200
    posts = response.json()
    for post in posts:
        try:
            PostSchema(**post)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed: {e}")


@pytest.mark.api
@pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/users"])
def test_multiple_endpoints(api_base_url, endpoint):
    response = requests.get(f"{api_base_url}{endpoint}")
    assert response.status_code == 200
    assert response.json()


@pytest.mark.api
def test_fetch_first_5_posts(api_base_url):
    response = requests.get(f"{api_base_url}/posts")
    assert response.status_code == 200
    
    posts = response.json()
    assert len(posts) > 0
    
    required_keys = {"userId", "id", "title", "body"}
    for post in posts:
        assert required_keys.issubset(post.keys())
    
    output_file = os.path.join(os.path.dirname(__file__), "..", "first_5_posts.json")
    with open(output_file, "w") as f:
        json.dump(posts[:5], f, indent=4)
    
    with open(output_file, "r") as f:
        saved_posts = json.load(f)
    
    assert len(saved_posts) == 5
