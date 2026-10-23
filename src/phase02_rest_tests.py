
import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def print_result(operation, response):
    print(f"\n{'=' * 50}")
    print(f"Operation: {operation}")
    print(f"Method: {response.request.method}")
    print(f"URL: {response.url}")
    print(f"Status Code: {response.status_code}")

    try:
        data = response.json()
        print("Response Body:")
        print(json.dumps(data, indent=2))
    except ValueError:
        print("Response Body:")
        print(response.text or "(empty response body)")


def run_tests():
    # Task 06: GET three individual posts
    for post_id in [1, 2, 3]:
        response = requests.get(
            f"{BASE_URL}/posts/{post_id}",
            headers={"Accept": "application/json"},
            timeout=TIMEOUT,
        )
        print_result(f"GET post {post_id}", response)

    # Task 07: POST a new post
    new_post = {
        "title": "My API Lab",
        "body": "Testing POST request",
        "userId": 1,
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=new_post,
        timeout=TIMEOUT,
    )
    print_result("POST new post", response)

    # Task 08: PUT an updated post
    updated_post = {
        "id": 1,
        "title": "Updated API Lab",
        "body": "Testing PUT request",
        "userId": 1,
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=updated_post,
        timeout=TIMEOUT,
    )
    print_result("PUT post 1", response)

    # Task 09: DELETE a post
    response = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=TIMEOUT,
    )
    print_result("DELETE post 1", response)

    # Task 10: Explicitly test a missing resource
    response = requests.get(
        f"{BASE_URL}/posts/999999",
        timeout=TIMEOUT,
    )
    print_result("GET nonexistent post", response)


if __name__ == "__main__":
    try:
        run_tests()
    except requests.exceptions.Timeout:
        print("A request timed out. Please retry.")
    except requests.exceptions.RequestException as error:
        print(f"Network/API request failed: {error}")
