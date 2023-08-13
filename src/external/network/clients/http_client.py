from abc import ABC, abstractclassmethod

from httpx import AsyncClient

class HttpClient(ABC):
    @abstractclassmethod
    async def configuration(self) -> AsyncClient:
        pass

class HttpClientImpl(HttpClient):
    __headers: dict[str, str] = {
        "apiKey": ""
    }

    async def configuration(self) -> AsyncClient:
        return AsyncClient(
            headers=self.__headers,
            base_url="",
        )
