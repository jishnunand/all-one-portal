import logging

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from pydantic.error_wrappers import ValidationError

from .pydantic_model import GitCreateModel
from github_config.views import create_git_repo


LOGGER = logging.getLogger(__name__)


class CreateRepo(APIView):
    """

    """
    def post(self, request):
        """

        :param request:
        :return:
        """
        try:
            request_data = GitCreateModel(**request.data)
        except ValidationError:
            response = {"message": "Bad Request data"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        if create_git_repo(org_name=request_data.org_name,
                           repo_name=request_data.repo_name,
                           description=request_data.description):
            response = {"message": "Repo Created Successfully"}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {"message": "Repo Creation Failed"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
