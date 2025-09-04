from abc import ABC, abstractmethod

from clientservices import MistralEmbeddingResponseModel


class EmbeddingServiceImpl(ABC):

    @abstractmethod
    async def ConvertTextToEmbedding(
        self, text: list[str]
    ) -> MistralEmbeddingResponseModel:
        pass
