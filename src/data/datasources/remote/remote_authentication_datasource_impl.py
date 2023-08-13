from result import Result, Ok, Err

from httpx import HTTPError, Response

from src.external.network.clients.http_client import HttpClient

from src.external.network.requests.sign_in_request import SignInRequest
from src.external.network.responses.message_response import MessageResponse
from src.external.network.responses.autentication_response import AuthenticationResponse

from src.domain.datasources.remote.remote_authentication_datasource import (
    RemoteAuthenticationDatasource
)

class RemoteAuthenticationDatasourceImpl(RemoteAuthenticationDatasource):
    def __init__(self, client: HttpClient) -> None:
        self.__client = client

    async def sign_in(
            self,
            parameter: SignInRequest
        ) -> Result[MessageResponse, AuthenticationResponse]:
        client = await self.__client.configuration()

        try:
            async with client:
                response = await client.post(
                    url="/auth/v1/token?grant_type=password",
                    data=parameter.model_dump_json()
                )

            return self.__parse_response(response)
        except HTTPError:
            Err(
                MessageResponse(
                    msg="Message",
                    error="Error",
                    error_description="Error Description",
                )
            )

    def __parse_response(
            self,
            response: Response
        ) -> Result[MessageResponse, AuthenticationResponse]:
        data = response.json()

        match response.status_code:
            case 200 | 201:
                return Ok(AuthenticationResponse.from_json(data))
            case 400 | 401:
                return Err(MessageResponse.from_json(data, True))
            case _:
                return Err(MessageResponse.from_json(data))
