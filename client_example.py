import requests
import json

# Base URL for the API
BASE_URL = 'http://localhost:5000'

def test_api():
    """Test the API endpoints"""
    print("🧪 Testing API endpoints...\n")
    
    # Test home endpoint
    print("1. Testing home endpoint...")
    try:
        response = requests.get(f'{BASE_URL}/')
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}\n")
    except Exception as e:
        print(f"   Error: {e}\n")
    
    # Test health endpoint
    print("2. Testing health endpoint...")
    try:
        response = requests.get(f'{BASE_URL}/health')
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}\n")
    except Exception as e:
        print(f"   Error: {e}\n")
    
    # Test creating a user
    print("3. Testing user creation...")
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    try:
        response = requests.post(
            f'{BASE_URL}/users',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(user_data)
        )
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}\n")
    except Exception as e:
        print(f"   Error: {e}\n")
    
    # Test getting users
    print("4. Testing getting users...")
    try:
        response = requests.get(f'{BASE_URL}/users')
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}\n")
    except Exception as e:
        print(f"   Error: {e}\n")

if __name__ == "__main__":
    test_api()