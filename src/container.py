from github import Github, Auth
from os import environ
from repo import RepoData


github_client = None
github_user = None
GITHUB_TOKEN = environ.get("GITHUB_TOKEN")


def get_github_user(github_token: str):
    """
    This function takes a Github token and returns a Github user.
    """
    global github_client
    global github_user
    if github_client is None:
        auth = Auth.Token(github_token)
        github_user = Github(auth=auth).get_user()
    return github_user

def get_repo_data() -> RepoData:
    """
    This function returns an instance of the RepoData class.
    """
    return RepoData(get_github_user(github_token=GITHUB_TOKEN))