import logging
from django.shortcuts import render
from django.conf import settings

from github import Github

# Get an instance of a logger
LOGGER = logging.getLogger(__name__)


class GitHubConfig:
    def __init__(self):
        try:
            self.connection = Github(settings.GITHUB_TOKEN)
            self.user = self.connection.get_user()
        except Exception as error:
            LOGGER.exception("Exception while trying to connect with github")
            self.connection = None
            self.user = None
        # Github Enterprise with custom hostname
        # Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

    def create_repo(self, repo_name):
        repo_status = self.user.create_repo(repo_name)

    def create_organisation_repo(self, org_name, repo_name, description):
        org_obj = self.connection.get_organization(org_name)
        org_obj.create_repo(
            repo_name,
            allow_rebase_merge=True,
            auto_init=False,
            description=description,
            has_issues=True,
            has_projects=False,
            has_wiki=False,
            private=True,
        )


def create_git_repo(org_name, repo_name, description):
    is_created = False
    git_config_obj = GitHubConfig()
    if git_config_obj.connection:
        try:
            git_config_obj.create_organisation_repo(org_name, repo_name, description)
            is_created = True
        except Exception as error:
            LOGGER.exception("Error while creating error")
    return is_created
