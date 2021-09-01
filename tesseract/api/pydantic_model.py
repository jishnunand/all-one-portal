from pydantic import BaseModel, ValidationError, validator


class GitCreateModel(BaseModel):
    org_name: str
    repo_name: str
    description: str
