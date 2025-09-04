from fastapi import APIRouter
from server.services import EmbeddingService
from fastapi.responses import JSONResponse
from server.models import ConvertTextToEmbeddingResponseModel

router = APIRouter()


embeddingService = EmbeddingService()


@router.post("/cte")
async def convertTextToEmbeddings(
    request: ConvertTextToEmbeddingResponseModel,
) -> JSONResponse:
    try:
        return await embeddingService.ConvertTextToEmbedding(text=request.texts)
    except Exception as e:
        print(e)
        return JSONResponse(content={"data": "SERVER_ERROR"}, status_code=500)
