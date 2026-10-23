
import os
from dotenv import load_dotenv

# Load variables from the .env file in the project root
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

print("TASK 17: AUTHORIZATION HEADER")

if API_TOKEN:
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json"
    }
    print("Authorization header created.")
    print("Bearer token is configured.")
else:
    headers = {
        "Accept": "application/json"
    }
    print("No API_TOKEN configured.")
    print("Authorization header was not created.")

print("\nTASK 18: SECURITY PRACTICES")
print("1. Keep credentials in environment variables.")
print("2. Never commit real tokens to Git.")
print("3. Use HTTPS for protected API requests.")
print("4. Give tokens only the permissions they need.")
print("5. Handle authentication failures safely.")
