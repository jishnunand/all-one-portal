import logging
from django.shortcuts import render
from django.conf import settings

from github import Github
from github.GithubException import UnknownObjectException
from github_config.utils import dict_to_yaml_convert

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

    def get_repo(self, organization=None, repo_name=None):
        repo = None
        if organization:
            repo = "{}/{}".format(organization, repo_name)
        elif repo_name:
            repo = repo_name
        else:
            return False
        try:
            repo_object = self.connection.get_repo(repo)
            return repo_object
        except UnknownObjectException:
            return False

    def create_repo(self, repo_name):
        repo_status = self.user.create_repo(repo_name)

    def create_organisation_repo(self, org_name, repo_name, description, app_name):
        org_name = org_name.replace(" ", "_")
        repo_name = "pc_{}".format(repo_name.replace(" ", "_"))
        org_obj = self.connection.get_organization(org_name)
        if not self.get_repo(organization=org_name, repo_name=repo_name):
            org_obj.create_repo(
                repo_name,
                description=description
            )
            self.create_file_in_repo(is_app=True, app_name=app_name)

    def create_file_in_repo(self, is_app=True, app_name=None):
        if is_app:
            app_name = app_name.replace(" ", "_")
            file_name = "{}/{}.yaml".format(app_name, app_name)
            yaml_data = dict_to_yaml_convert(in_app_name=True)
            self.connection.create_file(file_name, "Initial Commit", yaml_data, branch="main")


def create_git_repo(org_name=None, repo_name=None, description=None, app_name=None):
    is_created = False
    git_config_obj = GitHubConfig()
    if git_config_obj.connection:
        try:
            git_config_obj.create_organisation_repo(org_name, repo_name, description, app_name)
            is_created = True
        except Exception as error:
            LOGGER.exception("Error while creating error")
    return is_created
