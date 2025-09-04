from pydantic import BaseModel
from enums import ResponseEnums


class MistralEmbeddingUsageModel(BaseModel):
    promptTokens: int | None
    completionTokens: int | None
    totalTokens: int | None


class MistralEmbeddingDataModel(BaseModel):
    index: int | None
    embedding: list[float] | None


class MistralEmbeddingResponseModel(BaseModel):
    status: ResponseEnums = ResponseEnums.SUCCESS
    id: str | None = None
    model: str | None = None
    usage: MistralEmbeddingUsageModel | None = None
    data: list[MistralEmbeddingDataModel] | None = None
