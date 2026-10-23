
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_not_found():
    """Request a resource that should not exist."""
    url = f"{BASE_URL}/posts/999999"

    try:
        response = requests.get(url, timeout=5)

        print("TASK 19: 404 TEST")
        print("URL:", url)
        print("Status code:", response.status_code)

        if response.status_code == 404:
            print("Expected result: resource not found.")
        else:
            print("Received a different status code.")

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)


def test_timeout():
    """Demonstrate a request with a short timeout."""
    url = f"{BASE_URL}/posts/1"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        print("\nTASK 20: TIMEOUT HANDLING")
        print("Request succeeded.")
        print("Status code:", response.status_code)

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)


if __name__ == "__main__":
    test_not_found()
    test_timeout()
