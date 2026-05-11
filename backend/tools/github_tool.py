from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))


def search_github_repos(query: str):

    results = []

    try:

        repos = g.search_repositories(query=query)

        repo_list = repos.get_page(0)

        for repo in repo_list[:5]:

            results.append({

                "name": repo.full_name,

                "url": repo.html_url,

                "stars": repo.stargazers_count,

                "description": repo.description
                if repo.description
                else "No description provided."
            })

    except Exception as e:

        print(f"\nGITHUB SEARCH ERROR:\n{e}")

    return results