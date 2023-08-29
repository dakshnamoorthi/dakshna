import requests

# Replace 'YOUR_USERNAME' with your actual GitHub username
username = 'YOUR_USERNAME'

# GitHub API endpoint for user repositories
url = f'https://api.github.com/users/{username}/repos'

# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    repositories = response.json()
    print(f"Repositories for user '{username}':")
    for repo in repositories:
        print(repo['name'])
else:
    print(f"Failed to retrieve repositories. Status code: {response.status_code}")
print("dakshna")
print("abi")
print("tharun")

