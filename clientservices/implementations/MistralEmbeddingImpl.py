from abc import ABC, abstractmethod

from clientservices.models import MistralEmbeddingResponseModel


class MistralEmbeddingImpl(ABC):

    @abstractmethod
    async def ConvertTextToEmbedding(
        self, text: list[str]
    ) -> MistralEmbeddingResponseModel:
        pass
