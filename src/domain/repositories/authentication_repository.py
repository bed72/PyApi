from abc import ABC, abstractclassmethod

from result import Result, Ok, Err

from src.domain.models.message_model import MessageModel
from src.domain.parameters.sign_in_parameter import SignInParameter
from src.domain.models.autentication_model import AuthenticationModel
from src.external.network.requests.sign_in_request import SignInRequest
from src.external.network.responses.message_response import MessageResponse
from src.external.network.responses.autentication_response import AuthenticationResponse
from src.data.datasources.remote.remote_authentication_datasource_impl import (
    RemoteAuthenticationDatasource
)

class AuthenticationRepository(ABC):
    @abstractclassmethod
    async def sign_in(
        self, parameter: SignInParameter
    ) -> Result[MessageModel, AuthenticationModel]: pass

class AuthenticationRepositoryImpl(AuthenticationRepository):
    def __init__(self, datasource: RemoteAuthenticationDatasource) -> None:
        self.__datasource = datasource

    async def sign_in(
            self,
            parameter: SignInParameter
        ) -> Result[MessageModel, AuthenticationModel]:
        response = await self.__datasource.sign_in(self.__request(parameter))

        return Err(self.__failure(response.err())) if response.is_err() else Ok(self.__success(response.ok()))

    def __request(self, request: SignInParameter) -> SignInRequest:
        return SignInRequest(email=request.email, password=request.password)

    def __failure(self, failure: MessageResponse) -> MessageModel:
        return MessageModel(message=self.__format(failure))

    def __format(self, failure: MessageResponse) -> str:
        message = ''

        if failure.msg is not None:
            message = failure.msg

        if failure.error is not None:
            message = failure.error

        if failure.error_description is not None:
            message = failure.error_description

        return message

    def __success(self, success: AuthenticationResponse) -> AuthenticationModel:
        return AuthenticationModel(
            name=success.user.user_metadata.name,
            email=success.user.email,
            expires_in=success.expires_in,
            access_token=success.access_token,
            refresh_token=success.refresh_token
        )
