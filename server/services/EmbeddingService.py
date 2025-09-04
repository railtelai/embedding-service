from server.implementations import EmbeddingServiceImpl
from clientservices import MistralEmbeddingResponseModel
from clientservices import MistralEmbeddingService
from fastapi.responses import JSONResponse

mistralEmbeddingService = MistralEmbeddingService()


class EmbeddingService(EmbeddingServiceImpl):

    async def ConvertTextToEmbedding(self, text: list[str]) -> JSONResponse:

        embeddingResponse: MistralEmbeddingResponseModel = (
            await mistralEmbeddingService.ConvertTextToEmbedding(text=text)
        )

        return JSONResponse(
            content={
                "data": embeddingResponse.status.value[1],
                "embeddings": (
                    [e.model_dump() for e in embeddingResponse.data]
                    if embeddingResponse.data
                    else None
                ),
                "usage": (
                    embeddingResponse.usage.model_dump()
                    if embeddingResponse.usage
                    else None
                ),
            },
            status_code=embeddingResponse.status.value[0],
        )
