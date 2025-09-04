from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse


class EmbeddingServiceImpl(ABC):

    @abstractmethod
    async def ConvertTextToEmbedding(self, text: list[str]) -> JSONResponse:
        pass
