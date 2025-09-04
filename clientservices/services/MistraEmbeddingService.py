from mistralai import Mistral, models, EmbeddingResponse
from clientservices.implementations import MistralEmbeddingImpl
from clientservices.models import (
    MistralEmbeddingResponseModel,
    MistralEmbeddingDataModel,
    MistralEmbeddingUsageModel,
)
from clientservices.workers import GetMistralApiKey
from enums import ResponseEnums


mistralClient = Mistral(api_key=GetMistralApiKey())


class MistralEmbeddingService(MistralEmbeddingImpl):
    async def ConvertTextToEmbedding(
        self, text: list[str]
    ) -> MistralEmbeddingResponseModel:
        try:
            res: EmbeddingResponse = await mistralClient.embeddings.create_async(
                model="mistral-embed",
                inputs=text,
            )

            data = [
                MistralEmbeddingDataModel(
                    embedding=obj.embedding,
                    index=obj.index,
                )
                for obj in res.data
            ]
            usage = MistralEmbeddingUsageModel(
                completionTokens=res.usage.completion_tokens,
                promptTokens=res.usage.prompt_tokens,
                totalTokens=res.usage.total_tokens,
            )

            return MistralEmbeddingResponseModel(
                data=data,
                usage=usage,
                id=res.id,
                status=ResponseEnums.SUCCESS,
            )

        except models.HTTPValidationError as e:
            print(e)
            return MistralEmbeddingResponseModel(status=ResponseEnums.VALIDATION_ERROR)
        except models.SDKError as e:
            print(e)

            return MistralEmbeddingResponseModel(status=ResponseEnums.SERVER_ERROR)
