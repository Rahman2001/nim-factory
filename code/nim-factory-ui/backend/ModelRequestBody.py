from pydantic import BaseModel


class ModelRequestBody(BaseModel):
    family: str
    version: str
    type: str | None = None
