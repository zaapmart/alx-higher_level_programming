#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API
to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Takes your GitHub credentials (username and password) and uses the GitHub API
    to display your id
    """
    username = argv[1]
    password = argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_info = response.json()
        print("Your GitHub id is:", user_info['id'])
    else:
        print("Failed to fetch user information. Status code:", response.status_code)
