from typing import Dict
import logging
from json import dump
from os import makedirs, path


class RepoData:
    def __init__(self, get_github_user):
        self.github_user = get_github_user

    def get_repo_stats(self) -> Dict[str, str]:
        """
        This function returns a dictionary containing the repository name 
        and the number of commits.
        """
        repo_stats = {}
        logging.info("Requesting repository stats")
        for repo in self.github_user.get_repos():
            name = repo.name
            repo_stats[name] = {
                "created_at": repo.created_at,
                "private": repo.private,
                "forks_count": repo.forks_count,
                "stars_count": repo.stargazers_count,
                "watchers_count": repo.watchers_count,
                "deployments_count": repo.get_deployments().totalCount,
                "issues_count": repo.get_issues().totalCount,
                "commits_count": repo.get_commits().totalCount
            }
        logging.info("Repository stats retrieved")
        return repo_stats

    def get_repo_languages(self) -> Dict[str, Dict[str, float]]:
        """
        This function returns a dictionary containing the repository name 
        and the languages used in the repository.
        """
        repo_languages = {}
        logging.info("Requesting repository languages")
        for repo in self.github_user.get_repos():
            name = repo.name
            languages = repo.get_languages()
            total_bytes = sum(languages.values())
            language_percentages = {language: round((bytes_of_code / total_bytes) * 100, 2) for language, bytes_of_code in languages.items()}
            repo_languages[name] = language_percentages
        logging.info("Repository languages retrieved")
        return repo_languages

    def get_repo_commits(self) -> Dict[str, Dict[str, str]]:
        """
        This function returns a dictionary containing the repository name
        and the commits in the repository.
        """
        repo_commits = {}
        logging.info("Requesting repository commits")
        for repo in self.github_user.get_repos():
            name = repo.name
            commits = repo.get_commits(author=self.github_user.login)
            commit_details = {commit.commit.author.date for commit in commits}
            repo_commits[name] = commit_details
        logging.info("Repository commits retrieved")
        return repo_commits

    # function to save all the stats as json to /data folder
    def save_repo_stats(self):
        """
        This function saves the repository stats as a JSON file.
        """
        try:
            # Ensure the directory exists
            data_dir = "/github_analysis/src/data"
            makedirs(data_dir, exist_ok=True)
            logging.info("Directory '%s' created or already exists", data_dir)

            logging.info("Getting repository stats 1 of 3: Repository stats")
            repo_stats = self.get_repo_stats()
            with open(path.join(data_dir, "repo_stats.json"), "w", encoding="utf-8") as f:
                dump(repo_stats, f, default=str)
            logging.info("Repository stats saved")

            logging.info("Getting repository stats 2 of 3: Repository languages")
            repo_languages = self.get_repo_languages()
            with open(path.join(data_dir, "repo_languages.json"), "w", encoding="utf-8") as f:
                dump(repo_languages, f, default=str)
            logging.info("Repository languages saved")

            logging.info("Getting repository stats 3 of 3: Repository commits")
            repo_commits = self.get_repo_commits()
            with open(path.join(data_dir, "repo_commits.json"), "w", encoding="utf-8") as f:
                dump(repo_commits, f, default=str)
            logging.info("Repository commits saved")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
