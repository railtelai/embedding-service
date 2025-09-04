from pydantic import BaseModel


class ConvertTextToEmbeddingResponseModel(BaseModel):
    texts: list[str]
