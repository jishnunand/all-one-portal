from pydantic import BaseModel, ValidationError, validator


class GitCreateModel(BaseModel):
    org_name: str
    team_name: str
    description: str
    app_name: str
