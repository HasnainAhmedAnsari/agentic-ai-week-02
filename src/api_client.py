
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def get_post(post_id):
    """Retrieve one post and print its important fields."""
    url = f"{BASE_URL}/posts/{post_id}"

    try:
        response = requests.get(url, timeout=TIMEOUT)

        print(f"\nGET {url}")
        print("Status:", response.status_code)

        if response.status_code == 404:
            print("Post not found.")
            return None

        response.raise_for_status()
        post = response.json()

        print("ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])

        return post

    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")

    return None


def get_multiple_posts(post_ids):
    """Retrieve multiple posts using a loop."""
    print("\n--- MULTIPLE POSTS ---")

    posts = []

    for post_id in post_ids:
        post = get_post(post_id)

        if post is not None:
            posts.append(post)

    print(f"\nSuccessfully retrieved {len(posts)} posts.")
    return posts


def get_all_posts():
    """Retrieve the full collection and print its count and first five titles."""
    url = f"{BASE_URL}/posts"

    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()

        posts = response.json()

        print("\n--- ALL POSTS ---")
        print("Total posts returned:", len(posts))
        print("\nFirst five post titles:")

        for post in posts[:5]:
            print(f"{post['id']}. {post['title']}")

        return posts

    except requests.exceptions.Timeout:
        print("Request timed out while retrieving all posts.")
    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")
    except ValueError:
        print("The response was not valid JSON.")

    return []


if __name__ == "__main__":
    # Task 13: Retrieve one post
    get_post(1)

    # Task 14: Retrieve posts 1, 2 and 3
    get_multiple_posts([1, 2, 3])

    # Task 15: Retrieve and count the complete collection
    get_all_posts()
