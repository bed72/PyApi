from abc import ABC, abstractclassmethod

from result import Result

from src.external.network.requests.sign_in_request import SignInRequest
from src.external.network.responses.message_response import MessageResponse
from src.external.network.responses.autentication_response import AuthenticationResponse

class RemoteAuthenticationDatasource(ABC):
    @abstractclassmethod
    async def sign_in(self, parameter: SignInRequest) -> Result[MessageResponse, AuthenticationResponse]:
        pass
