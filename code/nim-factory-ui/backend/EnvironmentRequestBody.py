from ModelRequestBody import ModelRequestBody
from pydantic import BaseModel


class EnvironmentRequestBody(BaseModel):
    huggingface: dict | None = None
    model: ModelRequestBody
