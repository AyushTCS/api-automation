import requests
import json


BASE_URL = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(BASE_URL)
assert response.status_code == 200, f"Expected 200, got {response.status_code}"
posts = response.json()

required_keys = {"userId", "id", "title", "body"}
for post in posts:
    assert required_keys.issubset(post.keys()), f"Missing keys in post: {post}"

with open("first_5_posts.json", "w") as f:
    json.dump(posts[:5], f, indent=4)

