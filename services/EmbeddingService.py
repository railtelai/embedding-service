from implementations import EmbeddingServiceImpl
from clientservices import MistralEmbeddingResponseModel


class EmbeddingService(EmbeddingServiceImpl):

    def convertTextToEmbeddings(self) -> MistralEmbeddingResponseModel:
        pass
