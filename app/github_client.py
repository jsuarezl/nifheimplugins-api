import os

import requests
from fastapi import status


async def fetch_repository_tags(username: str, repository: str) -> list[str]:
    url = f"https://api.github.com/repos/{username}/{repository}/tags"
    response = requests.get(url, headers={'Accept': 'application/vnd.github.v3+json', 'Authorization': f'Bearer {os.getenv("GITHUB_TOKEN")}', 'X-GitHub-Api-Version': '2022-11-28'})
    if response.status_code == status.HTTP_200_OK:
        return list(map(lambda tag: tag['name'], response.json()))
    return []
